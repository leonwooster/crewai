import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Load environment variables from .env file
load_dotenv()

# Get the OPENAI_MODEL_NAME from the environment
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about certain topics",
    backstory="I am an information agent, I am here to help you with any information you need.",
)

task1 = Task(
    description="Tell me about the history of the internet",
    expected_output="The history of the internet is long and complex, but it started in the 1960s with the development of ARPANET, a network that connected computers at research institutions in the United States. Over the years, the internet has grown to become a global network that connects billions of people around the world.",   
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose= True
)

result= crew.kickoff()

print("---------------------------------------------------")
print(result)