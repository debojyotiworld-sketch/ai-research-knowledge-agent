from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agent import run_agent


app = FastAPI(
    title="AI Research Agent API",
    version="0.1.0",
)


class ResearchRequest(BaseModel):
    message: str


class ResearchResponse(BaseModel):
    response: str


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):
    try:
        response = run_agent(request.message)
        return {"response": response}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except RuntimeError as error:
        raise HTTPException(status_code=500, detail=str(error))