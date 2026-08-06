from db.pinecone_db import search_vectors

def retrieve_context(query_embedding, repo_name):

  response = search_vectors(query_embedding=query_embedding, repo_name=repo_name)
  if response is None or not response.matches:
    return []

  contexts = []

  for match in response.matches:
    contexts.append({
      "score": match.score,
      "name": match.metadata["name"],
      "file_path": match.metadata["file_path"],
      "content": match.metadata["content"],
      "type": match.metadata["type"],
      "start_line": match.metadata["start_line"],
      "end_line": match.metadata["end_line"]
      })
  # print(contexts)
  return contexts