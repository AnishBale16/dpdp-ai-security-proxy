def mock_llm_response(prompt: str):

    return {
        "model": "mock-llm",
        "response": f"Mock AI response for: {prompt}"
    }
