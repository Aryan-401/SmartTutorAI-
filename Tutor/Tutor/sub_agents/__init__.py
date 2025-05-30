from .math_agent.agent import root_agent as math_agent
from .physics_agent.agent import root_agent as physics_agent
from .chemistry_agent.agent import root_agent as chemistry_agent
from .english_agent.agent import root_agent as english_agent


__all__ = ["math_agent", "physics_agent", "chemistry_agent", "english_agent"]