from fastapi import FastAPI
from schemas import GitHubRequest, QueryRequest
from services.extraction.git_extraction import git_extraction
from services.embedding import embed_query
from services.llm import ask_llm
from services.retrieval import retrieve_context
from services.prompt_builder import build_prompt

app = FastAPI(title="AI Codebase Assistant", version="1.0.0")


@app.get("/")
def home():
  return {"message": "AI Codebase Assistant API"}


@app.post("/ingest")
def ingest_repo(request: GitHubRequest):
  git_extraction(request.repo_url)

  return {
        "status": "success",
        "message": "Repository indexed successfully."
    }

@app.post("/query")
def query(request: QueryRequest):

  query_vector = embed_query(request.query)
  
  contexts = retrieve_context(query_vector,request.repo_name)
  
  prompt = build_prompt(request.query, contexts)
  
  answer = ask_llm(prompt)

  return {
    "answer": answer,
    "references": contexts
    }
  
  # results = search_vectors(query_vector)

  # return results

  # return {
  #   "query": request.query,
  #   "dimension": len(query_vector),
  #   "embedding": query_vector
  # }