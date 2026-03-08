from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class TeacherAssistantCrewai():
    """Teacher Assistant Crew — generates lesson plans, quizzes, and teaching suggestions."""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ── Agents ────────────────────────────────────────────────────────────────

    @agent
    def lesson_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['lesson_planner'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def quiz_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_generator'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def teaching_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['teaching_advisor'],  # type: ignore[index]
            verbose=True
        )

    # ── Tasks ─────────────────────────────────────────────────────────────────

    @task
    def lesson_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['lesson_plan_task'],  # type: ignore[index]
            output_file='output/lesson_plan.md'
        )

    @task
    def quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config['quiz_task'],  # type: ignore[index]
            output_file='output/quiz.md'
        )

    @task
    def teaching_suggestions_task(self) -> Task:
        return Task(
            config=self.tasks_config['teaching_suggestions_task'],  # type: ignore[index]
            output_file='output/teaching_suggestions.md'
        )

    # ── Crew ──────────────────────────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the Teacher Assistant crew."""
        return Crew(
            agents=self.agents,   # populated by @agent decorators
            tasks=self.tasks,     # populated by @task decorators
            process=Process.sequential,
            verbose=True,
        )
