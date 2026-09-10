from pathlib import Path
from ..chunker import code_chunker
from ..embedding import embedding_chunks

def extract_contents(path, repo_name):
  directory = Path(path)
  
  modules = list(directory.rglob("*.py"))
  
  print("Python files found:", len(modules))

    # for m in modules:
    #   print(m)
    
  documents = []
  all_chunks = []
  
  for module in modules:
    content = module.read_text(encoding="utf-8", errors="ignore")
    documents.append({
      "path":str(module),
      "content":content
    })
  # print(documents)
  
  for docs in documents:
    chunks = code_chunker(docs)
    all_chunks.extend(chunks)
    # print("all_chunks", all_chunks)
    
  embedding_results = embedding_chunks(all_chunks, repo_name)
  return {
    "python_files": len(modules),
    "chunks": len(all_chunks),
    "embedding_result": embedding_results
  }
  