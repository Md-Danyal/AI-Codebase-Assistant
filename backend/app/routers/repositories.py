from fastapi import APIRouter
from backend.app.schemas import GitHubRequest
from services.extraction.git_extraction import git_extraction


router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)

@router.post("/ingest")
def ingest_repo(request: GitHubRequest):
    repo_name = str(request.repo_url).rstrip("/").split("/")[-1]
    result = git_extraction(str(request.repo_url))

    return {
        "status": "success",
        "message": "Repository indexed successfully.",
        "repository": {"repo_name": repo_name, "url": str(request.repo_url)},
        "repo_url": str(request.repo_url),
        "indexing": {
            "python_files": result["python_files"],
            "chunks": result["chunks"]
        }
    }