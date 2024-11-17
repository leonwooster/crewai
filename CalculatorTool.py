from crewai.tools import tool

@tool("Calculate")
def calculate(equation : str) -> float:
    """ Use this tool to calculate a given equation """
    return eval(equation)

# Define a custom tool for handling user input
@tool("UserInput")
def get_user_input(prompt: str) -> str:
    """ Use this tool to capture user input """
    return input(prompt)