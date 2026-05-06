import operator
from typing import Annotated, TypedDict, Any, Sequence
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next_agent: str
    user_id: str
    session_id: str
    memory_context: str
    metadata: dict[str, Any]

class AgentOutput(TypedDict):
    response: str
    tool_calls: list[dict[str, Any]]
    metadata: dict[str, Any]