from fastapi import FastAPI

from backend.app.routers.chat import router as chat_router
from backend.app.routers.repositories import router as repository_router


app = FastAPI(
    title="AI Codebase Assistant",
    version="2.0.0"
)

app.include_router(chat_router, prefix="/api/v1")

app.include_router(repository_router, prefix="/api/v1")

@app.get("/")
def home():
  return {"message": "AI Codebase Assistant API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

  # results = search_vectors(query_vector)

  # return results

  # return {
  #   "query": request.query,
  #   "dimension": len(query_vector),
  #   "embedding": query_vector
  # }