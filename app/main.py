from fastapi import FastAPI

app = FastAPI(title="DPDP AI Security Proxy")

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "DPDP AI Security Proxy"
    }

@app.get("/health")
def health():
    return {"health": "ok"}
