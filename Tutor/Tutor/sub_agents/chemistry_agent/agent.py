import os
from . import tools
from google.adk.agents import Agent

root_agent = Agent(
    name="chemistry_agent_v1",
    model= os.environ["MODEL_GEMINI_2_0_FLASH"], # LiteLlm(model=os.environ["MODEL_GEMINI_2_0_FLASH"]
    description="Balances chemical equations and provides information on chemical compounds.",
    instruction='You are an Agent that can balance chemical equations and provide information on chemical compounds.',
    tools=[tools.balance_equation],
)