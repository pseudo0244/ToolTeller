from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class DocReader():
	#CONFIG FILES 
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

#MY AGENTS

	#AGENT 1: PROCESSING THE INPUT TOOL
	@agent
	def input_tool(self) -> Agent:
		return Agent(
			config=self.agents_config['input_tool'],
			verbose=True
		)
	
	#AGENT 2: LATEST DOCUMENT SURFER
	@agent
	def doc_surfer(self) -> Agent:
		return Agent(
			config=self.agents_config['doc_surfer'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	#AGENT 3: LATEST DOCUMENT SUMMARISER
	@agent
	def doc_summary(self) -> Agent:
		return Agent(
			config=self.agents_config['doc_summary'],
			verbose=True
		)
	
	#AGENT 4: LATEST UPDATES SUMMARISER
	@agent
	def update_summary(self) -> Agent:
		return Agent(
			config=self.agents_config['update_summary'],
			verbose=True
		)
	
	#AGENT 4: FILE WRITER
	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
			tools=[FileWriterTool()],
			verbose=True
		)
	

#MY TASKS

	#TASK 1: INPUT TOOL PROCESSING TASK
	@task
	def input_tool_task(self) -> Task:
		return Task(
			config=self.tasks_config['input_tool_task'],
		)

	#TASK 2: DOCUMENT SURF TASK
	@task
	def doc_surf_task(self) -> Task:
		return Task(
			config=self.tasks_config['doc_surf_task'],
		)
	
	#TASK 3: DOCUMENT SUMMARY TASK
	@task
	def doc_summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['doc_summary_task'],
		)
	
	#TASK 4: LATEST UPDATES SUMMARY TASK
	@task
	def update_summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['update_summary_task'],
		)
	
	#TASK 5: FILE WRITER TASK
	@task
	def file_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_write_task'],
		)


#MY CREW
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
