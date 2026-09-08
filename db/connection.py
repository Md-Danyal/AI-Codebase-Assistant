# from dotenv import load_dotenv
# import os
from pinecone import Pinecone, ServerlessSpec
from backend.app.config import settings

# load_dotenv()

# PINECONE_API = os.getenv("PINECONE_API")
# GROQ_API = os.getenv("GROQ_API")

pc = Pinecone(settings.PINECONE_API_KEY)

def create_index():
  pc.create_index(
    name=settings.PINECONE_INDEX,
    dimension=1024,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)
  
# create_index()

index = pc.Index("codebase-assistant")

def upsert_vectors(vectors,repo_name):
  index.upsert(vectors=vectors,namespace=repo_name)
  
  print("Created")