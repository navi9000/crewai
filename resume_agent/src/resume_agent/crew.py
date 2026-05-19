from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class ResumeAgent():
    """ResumeAgent crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True
        )

    @agent
    def applicant(self) -> Agent:
        return Agent(
            config=self.agents_config['applicant'],
            verbose=True
        )

    @task
    def analyze_vacancy(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_vacancy'],
        )

    @task
    def write_letter(self) -> Task:
        return Task(
            config=self.tasks_config['write_letter'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeAgent crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
