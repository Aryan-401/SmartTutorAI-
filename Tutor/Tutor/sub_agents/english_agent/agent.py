import os
from google.adk.agents import Agent

root_agent = Agent(
    name="english_agent_v1",
    model= os.environ["MODEL_GEMINI_2_0_FLASH"], # LiteLlm(model=os.environ["MODEL_GEMINI_2_0_FLASH"]
    description="Provides English language assistance. You also Specialise in NCERT English, helping answer any questions related to the Reading and Poems in NCERT English.",
    instruction='You are an Agent that can assist with English language tasks, not only Language but also NCERT English reading and poems.',
    tools=[],
)