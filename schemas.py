from pydantic import BaseModel

class GitHubRequest(BaseModel):
  repo_url: str

class QueryRequest(BaseModel):
  repo_name: str
  query: str