from pydantic import BaseModel, HttpUrl

class GitHubRequest(BaseModel):
  repo_url: HttpUrl

class QueryRequest(BaseModel):
  conversation_id: str
  repo_name: str
  query: str