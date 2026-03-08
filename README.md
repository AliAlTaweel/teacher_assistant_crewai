# Teacher Assistant — AI-Powered Lesson Planning

An AI multi-agent system that helps teachers generate **lesson plans**, **quizzes**, and **teaching strategies** from raw subject notes — in minutes.

Built with [CrewAI](https://crewai.com), it orchestrates three specialized agents that collaborate sequentially to produce classroom-ready materials.

---

## How It Works

Three AI agents work together on your input:

| Agent | Role | Output |
|---|---|---|
| **Lesson Planner** | Curriculum designer with 15+ years experience | Structured lesson plan with objectives, activities & time estimates |
| **Quiz Generator** | Assessment specialist | Mixed-format quiz (MCQ, short answer, true/false) + answer key |
| **Teaching Advisor** | Pedagogical strategy coach | Teaching strategies, analogies, misconception fixes, formative assessment ideas |

**Flow:** Enter subject + notes → agents run sequentially → 3 markdown files saved to `output/`

---

## Demo

> Enter your subject and notes in the UI, click **Generate**, and get all three outputs in the tabs.

![UI screenshot placeholder]

---

## Setup

**Requirements:** Python 3.10–3.13, [uv](https://docs.astral.sh/uv/)

```bash
# 1. Install uv (if not already installed)
pip install uv

# 2. Install dependencies
crewai install

# 3. Add your API key to .env
echo "OPENAI_API_KEY=your_key_here" > .env
```

---

## Run

```bash
crewai run
```

Opens a Gradio UI at **http://localhost:7860**. Fill in the subject and your lesson notes, then click **Generate**.

Outputs are saved to:
```
output/
├── lesson_plan.md
├── quiz.md
└── teaching_suggestions.md
```

---

## Project Structure

```
src/teacher_assistant_crewai/
├── config/
│   ├── agents.yaml        # Agent roles, goals, and backstories
│   └── tasks.yaml         # Task descriptions and expected outputs
├── crew.py                # Crew definition and agent/task wiring
├── main.py                # Entry point (launches UI)
└── ui.py                  # Gradio web interface
```

---

## Tech Stack

- [CrewAI](https://crewai.com) — multi-agent orchestration
- [Gradio](https://gradio.app) — web UI
- [LiteLLM](https://litellm.ai) — LLM provider abstraction
- Python 3.12 / [uv](https://docs.astral.sh/uv/)
