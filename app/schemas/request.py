from pydantic import BaseModel

class AIRequest(BaseModel):
    prompt: str
    provider: str = "mock"
