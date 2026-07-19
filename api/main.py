from fastapi import FastAPI
from pydantic import BaseModel

from chatbot.conversation_engine import ConversationEngine
from manager.engine_manager import EngineManager

app = FastAPI(
    title="Prime AI Counsellor API",
    version="1.0"
)

engine_manager = EngineManager()


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def home():
    return {
        "message": "Prime AI Counsellor API is running."
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    engine = engine_manager.get_engine(request.user_id)
    answer = engine.chat(request.message)

    return ChatResponse(reply=answer)