#!/usr/bin/env python
"""Simple Gradio UI for the Teacher Assistant CrewAI."""

import os
import sys
import threading
import warnings
from pathlib import Path

import gradio as gr

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Ensure the output directory exists
Path("output").mkdir(exist_ok=True)

# ── Crew runner ───────────────────────────────────────────────────────────────

def run_crew(subject: str, notes: str):
    """Run the crew and stream results back."""
    if not subject.strip():
        yield "Please enter a subject.", "", "", ""
        return
    if not notes.strip():
        yield "Please enter some notes.", "", "", ""
        return

    yield "Running Teacher Assistant crew... this may take a few minutes.", "", "", ""

    try:
        from teacher_assistant_crewai.crew import TeacherAssistantCrewai

        inputs = {"subject": subject.strip(), "notes": notes.strip()}
        TeacherAssistantCrewai().crew().kickoff(inputs=inputs)

        lesson = Path("output/lesson_plan.md").read_text(encoding="utf-8") if Path("output/lesson_plan.md").exists() else "No output."
        quiz = Path("output/quiz.md").read_text(encoding="utf-8") if Path("output/quiz.md").exists() else "No output."
        suggestions = Path("output/teaching_suggestions.md").read_text(encoding="utf-8") if Path("output/teaching_suggestions.md").exists() else "No output."

        yield "Done!", lesson, quiz, suggestions

    except Exception as e:
        yield f"Error: {e}", "", "", ""


# ── UI ────────────────────────────────────────────────────────────────────────

EXAMPLE_SUBJECT = "Introduction to Fractions"
EXAMPLE_NOTES = """Topic: Fractions for Grade 5 students

Key concepts:
- A fraction represents a part of a whole (e.g., 1/2 means one out of two equal parts)
- Numerator: the top number — how many parts we have
- Denominator: the bottom number — how many equal parts the whole is divided into
- Equivalent fractions: different fractions that represent the same value (e.g., 1/2 = 2/4 = 4/8)
- Simplifying fractions: divide both numerator and denominator by their GCD
- Comparing fractions: use cross-multiplication or find a common denominator

Common student difficulties:
- Confusing numerator and denominator roles
- Adding denominators when adding fractions (WRONG: 1/2 + 1/3 = 2/5)
- Forgetting to simplify the final answer
"""

with gr.Blocks(title="Teacher Assistant") as demo:
    gr.Markdown("# 🎓 Teacher Assistant\nGenerate a **lesson plan**, **quiz**, and **teaching suggestions** using AI agents.")

    with gr.Row():
        with gr.Column(scale=1):
            subject_input = gr.Textbox(
                label="Subject / Topic",
                placeholder="e.g. Introduction to Fractions",
                value=EXAMPLE_SUBJECT,
            )
            notes_input = gr.Textbox(
                label="Lesson Notes",
                placeholder="Paste your notes here...",
                lines=12,
                value=EXAMPLE_NOTES,
            )
            run_btn = gr.Button("Generate", variant="primary")
            status = gr.Textbox(label="Status", interactive=False)

        with gr.Column(scale=2):
            with gr.Tabs():
                with gr.Tab("Lesson Plan"):
                    lesson_out = gr.Markdown()
                with gr.Tab("Quiz"):
                    quiz_out = gr.Markdown()
                with gr.Tab("Teaching Suggestions"):
                    suggestions_out = gr.Markdown()

    run_btn.click(
        fn=run_crew,
        inputs=[subject_input, notes_input],
        outputs=[status, lesson_out, quiz_out, suggestions_out],
    )


def launch():
    """Entry point for the UI."""
    demo.launch(theme=gr.themes.Soft())


if __name__ == "__main__":
    launch()
