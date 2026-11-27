from fastapi import FastAPI
from app.schemas.request import AIRequest

app = FastAPI()

@app.post("/api/v1/chat")
def chat(request: AIRequest):

    return {
        "received_prompt": request.prompt,
        "provider": request.provider,
        "status": "received"
    }
