from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class CrewaiDebate():
    """CrewaiDebate crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def debater(self) -> Agent:
        return Agent(
            config=self.agents_config['debater'], # type: ignore[index]
            verbose=True
        )

    @agent
    def adjudicator(self) -> Agent:
        return Agent(
            config=self.agents_config['adjudicator'], # type: ignore[index]
            verbose=True
        )

    @task
    def propose_task(self) -> Task:
        return Task(
            config=self.tasks_config['propose_task'], # type: ignore[index]
        )

    @task
    def oppose_task(self) -> Task:
        return Task(
            config=self.tasks_config['oppose_task'], # type: ignore[index]
        )

    @task
    def adjudicate_task(self) -> Task:
        return Task(
            config=self.tasks_config['adjudicate_task'], # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
