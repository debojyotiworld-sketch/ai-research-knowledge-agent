from fastapi import FastAPI
from pydantic import BaseModel

from agent import run_agent


app = FastAPI()


class ResearchRequest(BaseModel):
    query: str


@app.post("/research")
def research(request: ResearchRequest):
    result = run_agent(request.query)

    return {
        "answer": result
    }