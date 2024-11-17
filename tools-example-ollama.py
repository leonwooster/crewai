import os
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
from CalculatorTool import calculate, get_user_input

load_dotenv()

# Configure the LLM using Ollama
ollm = LLM(
    model="ollama/llama3.2-vision",  # Use the model name you pulled
    base_url="http://localhost:11434",  # Default port for Ollama
    temperature=0.7,  # Adjust temperature for creativity    
)

print("Welcome to Math Whiz! I am here to help you with any math problems you have.")

# Define an agent that uses this tool
input_agent = Agent(
    LLModel=ollm,
    role='Input Collector',
    goal='Collect user input for processing',
    backstory='I am here to collect user input for processing',
    verbose=True,
    tools=[get_user_input]
)

math_agent = Agent(
    LLM=ollm,
    role="Math Whiz",
    goal="Solve math problems",
    backstory="I am a math whiz, I am here to help you with any math problems you have.",
    verbose=True,
    tools=[calculate],    
)

writer = Agent(
    LLM=ollm,
    role="Writer",
    goal="Craft compelling explanations based from the output of the Math Whiz",
    backstory="I am a writer, I am here to help you understand the output of the Math Whiz.",
    verbose=True   
)

# Define a task that utilizes the agent to collect user input
input_task = Task(
    description="Get the math equation from user",
    expected_output="User feedback collected successfully",
    agent=input_agent,
)

task1 = Task(
    description="Solve the following equation",
    expected_output="Give full details in bullet points",
    agent=math_agent,
    context=[input_task]
)

task2 = Task(
    description="using the insights provided, explain in great details how the equation was solved",   
    expected_output="The equation was solved by using the following steps:",
    output_file="math.md",
    agent=writer,
    context=[task1]
)

crew = Crew(
    agents=[input_agent, math_agent, writer],
    tasks=[input_task, task1, task2],
    process=Process.sequential,
    verbose=True   
)

result = crew.kickoff()

print(result)