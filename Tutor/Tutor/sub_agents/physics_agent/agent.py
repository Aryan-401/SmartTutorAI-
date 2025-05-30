import os
from . import tools
from google.adk.agents import Agent

root_agent = Agent(
    name="physics_agent_v1",
    model= os.environ["MODEL_GEMINI_2_0_FLASH"], # LiteLlm(model=os.environ["MODEL_GEMINI_2_0_FLASH"]
    description="Provides physics constants and evaluates physics-related code.",
    instruction='You are an Agent which can provide physics constants. Currently supported constants are: PI, E, GOLDEN_RATIO, SPEED_OF_LIGHT, GRAVITATIONAL_CONSTANT.',
    tools=[tools.get_constants],
)
