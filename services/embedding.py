from sentence_transformers import SentenceTransformer
from db.pinecone_db import insert_vectors

embed_model = SentenceTransformer("BAAI/bge-m3")

def embedding_chunks(all_chunks, repo_name):
  texts = [chunk["content"] for chunk in all_chunks]
  
  embedding = embed_model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
  # print(embedding)
  print("-"*30)
  
  return insert_vectors(embedding,all_chunks, repo_name)

def embed_query(query: str):
  embedding = embed_model.encode(query, convert_to_numpy=True)

  return embedding.tolist()