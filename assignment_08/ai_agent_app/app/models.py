from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

class TaskType(Enum):
    RESEARCH = "research"
    ANALYSIS = "analysis"
    GENERAL = "general"

class TaskInput(BaseModel):
    task: str
    task_type: TaskType
    context: Optional[str] = None

class AgentResponse(BaseModel):
    response: str
    sources: Optional[List[str]] = None
    confidence: Optional[float] = None