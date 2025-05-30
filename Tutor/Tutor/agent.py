from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # For multi-model support
from .sub_agents import math_agent, physics_agent, chemistry_agent, english_agent
from . import tools
import warnings
import os


# Load environment variables
# load_dotenv("Tutor/.env")

# Ignore all warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)


root_agent = Agent(
    name="root_agent_v1",
    model= os.environ["MODEL_GEMINI_2_0_FLASH"], # LiteLlm(model=os.environ["MODEL_GEMINI_2_0_FLASH"]
    description="An AI Tutor that coordinates multiple sub-agents to solve complex problems in Physics, Math, Chemistry, and English. You also know the current date and weather.",
    instruction='You are an AI Tutor which is a specialist in Physics and Math. You are a coordinator of multiple sub-agents, each specialized in Physics or Math.'
                'Your agents can coordinate with each other to solve complex problems. Such as using the Physics `get_constants` tool to get the value of a constant and then using the Math `coder` tool to evaluate a code snippet that uses that constant.'
                'Your Sub-Agents:\n'
                '1. Math Agent: Has the ability to run code to solve most Math Problems. The math problems can only be solved if you can write python code for it.\n',

    tools=[tools.get_date, tools.get_weather],
    sub_agents=[
        math_agent,

    ]
)




