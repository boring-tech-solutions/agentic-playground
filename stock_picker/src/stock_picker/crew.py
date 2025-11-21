from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool

from typing import List

from .schemas.trending_company import (
    TrendingCompaniesListSchema,
    TrendingCompaniesResearchListSchema
)

@CrewBase
class StockPicker():
    """StockPicker crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_company_finder'], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def stock_picker(self)-> Agent:
        return Agent(
            config=self.agents_config['stock_picker'],
            verbose=True
        )

    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'], # type: ignore[index]
            output_pydantic=TrendingCompaniesListSchema
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'], # type: ignore[index]
            output_pydantic=TrendingCompaniesResearchListSchema
        )
    
    @task
    def pick_best_stock(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_stock']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StockPicker crew"""

        # We define the manager agent for hierarchical process
        manager = Agent(
            config=self.agents_config['manager'], # type: ignore[index]
            allow_delegation=True,
            verbose=True
        )

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager
        )
