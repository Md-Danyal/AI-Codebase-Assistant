from fastapi import APIRouter

from backend.app.schemas import QueryRequest

from services.embedding import embed_query
from services.llm import ask_llm
from services.prompt_builder import build_prompt
from services.retrieval import retrieve_context
from services.memory import get_conversation, add_message

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/query")
def query(request: QueryRequest):
  
  conversation = get_conversation(request.conversation_id)

  query_vector = embed_query(request.query)
  
  contexts = retrieve_context(query_vector,request.repo_name)
  
  prompt = build_prompt(request.query, contexts, conversation)

  answer = ask_llm(prompt)
  
  add_message(request.conversation_id, "user", request.query)
  add_message(request.conversation_id, "assistant", answer)
  
  references = [
    {
      "score": context["score"],
      "name": context["name"],
      "file_path": context["file_path"],
      "type": context["type"],
      "start_line": context["start_line"],
      "end_line": context["end_line"]
      }
    for context in contexts
    ]

  return {
    "conversation_id": request.conversation_id,
    "answer": answer,
    "references": references
    }