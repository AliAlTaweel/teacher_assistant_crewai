#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from teacher_assistant_crewai.crew import TeacherAssistantCrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_notes_from_file(filepath: str) -> str:
    """Read notes from a plain text file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Notes file not found: {filepath}")
    return path.read_text(encoding="utf-8")


def ensure_output_dir():
    """Make sure the output directory exists."""
    Path("output").mkdir(exist_ok=True)


# ── Entry points ──────────────────────────────────────────────────────────────

def run():
    """Launch the Teacher Assistant UI."""
    from teacher_assistant_crewai.ui import launch
    launch()


def train():
    """Train the crew for a given number of iterations."""
    ensure_output_dir()
    inputs = {
        "subject": "Introduction to Fractions",
        "notes": "Fractions represent parts of a whole. Numerator is on top, denominator on bottom.",
    }
    try:
        TeacherAssistantCrewai().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """Replay the crew execution from a specific task."""
    try:
        TeacherAssistantCrewai().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """Test the crew execution and return the results."""
    ensure_output_dir()
    inputs = {
        "subject": "Introduction to Fractions",
        "notes": "Fractions represent parts of a whole. Numerator is on top, denominator on bottom.",
    }
    try:
        TeacherAssistantCrewai().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
