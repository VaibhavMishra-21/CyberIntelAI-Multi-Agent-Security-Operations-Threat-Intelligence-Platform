from langgraph.graph import StateGraph

from models.state import SecurityState

workflow = StateGraph(
    SecurityState
)
