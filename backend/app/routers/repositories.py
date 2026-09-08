from fastapi import APIRouter
from backend.app.schemas import GitHubRequest
from services.extraction.git_extraction import git_extraction


router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)

@router.post("/ingest")
def ingest_repo(request: GitHubRequest):
  git_extraction(str(request.repo_url))

  return {
        "status": "success",
        "message": "Repository indexed successfully."
    }