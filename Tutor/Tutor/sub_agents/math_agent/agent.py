import os
from . import tools
from google.adk.agents import Agent

root_agent = Agent(
    name="math_agent_v1",
    model= os.environ["MODEL_GEMINI_2_0_FLASH"], # LiteLlm(model=os.environ["MODEL_GEMINI_2_0_FLASH"]
    description="Provides weather information for specific cities.",
    instruction='You are an Agent that can use Python to evaluate Math word problems, expressions and run code snippets. '
                'You will receive Python code as input, and you should evaluate it and return the output.'
                ' Do not add any ```python``` or other formatting to the output. Print the steps you are taking to solve the problem.'
                'You may reuse the same tool multiple times if needed. In case of word problems, you should first convert the problem into a Python code snippet and then evaluate it.',
    tools=[tools.coder],
)
