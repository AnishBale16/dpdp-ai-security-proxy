from app.proxy.provider import mock_llm_response

@app.post("/api/v1/chat")
def chat(request: AIRequest):

    result = mock_llm_response(request.prompt)

    return result
