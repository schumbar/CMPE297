from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime

from .agent import AIAgent
from .models import TaskInput, AgentResponse

# Initialize FastAPI app
app = FastAPI(title="AI Agent API")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Initialize agent
agent = AIAgent()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the frontend interface"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process", response_model=AgentResponse)
async def process_task_endpoint(task_input: TaskInput) -> AgentResponse:
    """Endpoint for processing tasks"""
    try:
        return await agent.process_task(task_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}