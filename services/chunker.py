import ast

def code_chunker(docs):
  code = docs["content"]
  code_chunks = []
  try:
    tree = ast.parse(code)
  except SyntaxError:
    return []
  for node in tree.body:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,ast.ClassDef)):
      chunk_type = "class" if isinstance(node, ast.ClassDef) else "function"
      content = ast.get_source_segment(code, node)
      
      if content is None:
        continue
      chunk = {
        "name": node.name,
        "type": chunk_type,
        "content": content,
        "file_path": docs["path"],
        "start_line": node.lineno,
        "end_line": node.end_lineno
      }
      
      code_chunks.append(chunk)
      
  return code_chunks