from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.pinecone_store import search_query
from app.llm import generate_answer


# Rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="HR Policy RAG Assistant")


class Question(BaseModel):
    question: str


# Home route (fixes 404 on "/")
@app.get("/")
def home():
    return {"message": "HR Policy RAG Assistant API is running"}


# Normal endpoint
@app.post("/ask")
@limiter.limit("10/minute")
def ask_question(data: Question):

    query = data.question

    context = search_query(query)

    answer = generate_answer(context, query)

    return {
        "question": query,
        "answer": answer
    }


# Streaming endpoint (for real-time response)
@app.post("/ask-stream")
def ask_question_stream(data: Question):

    query = data.question

    context = search_query(query)

    answer = generate_answer(context, query)

    def generate():

        for word in answer.split():
            yield word + " "

    return StreamingResponse(generate(), media_type="text/plain")