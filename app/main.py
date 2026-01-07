from fastapi import FastAPI
from app.schemas import FAQRequest, FAQResponse
from app.rag.retriever import retrieve_context
from app.rag.generator import generate_answer
from app.rag.memory import get_contextual_question, update_session

app = FastAPI()

@app.post("/api/ask-faq", response_model=FAQResponse)
def ask_faq(req: FAQRequest):
    question = req.question

    if req.session_id:
        question = get_contextual_question(req.session_id, question)

    context, sources = retrieve_context(question)
    answer = generate_answer(question, context)

    if req.session_id:
        update_session(req.session_id, question)

    return FAQResponse(answer=answer, sources=sources)
