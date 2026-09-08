from .connection import upsert_vectors,index

def insert_vectors(embedding,chunks, repo_name):
  vectors = []
  print(type(embedding))
  print(type(chunks))
  print(type(chunks[0]))
  
  for embedd,chunk in zip(embedding,chunks):
    vectors.append({
        "id": f"{chunk['file_path']}:{chunk['start_line']}",
        "values": embedd.tolist(),
        "metadata": {
            "name": chunk["name"],
            "type": chunk["type"],
            "content": chunk["content"],
            "file_path": chunk["file_path"],
            "start_line": chunk["start_line"],
            "end_line": chunk["end_line"]
        }
    })
    
  return upsert_vectors(vectors, repo_name=repo_name)

def search_vectors(query_embedding, repo_name):
  response = index.query(vector=query_embedding, top_k = 1, include_metadata= True, namespace=repo_name)
  
  # print(type(response))
  # print(response)
  return response