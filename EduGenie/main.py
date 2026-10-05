from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import generate_learning_path


app = FastAPI(title="EduGenie")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class TextRequest(BaseModel):
    text: str


class QuestionRequest(BaseModel):
    question: str


class TopicRequest(BaseModel):
    topic: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/qa")
async def qa(request: QuestionRequest):
    result = answer_question(request.question)
    return {"result": result}


@app.post("/explain")
async def explain(request: TopicRequest):
    result = explain_topic(request.topic)
    return {"result": result}


@app.post("/quiz")
async def quiz(request: TopicRequest):
    result = generate_quiz(request.topic)
    return {"result": result}


@app.post("/summarize")
async def summarize(request: TextRequest):
    result = summarize_text(request.text)
    return {"result": result}


@app.post("/learn/recommendations")
async def learning_recommendations(request: TopicRequest):
    result = generate_learning_path(request.topic)
    return {"result": result}