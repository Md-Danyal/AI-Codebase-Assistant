def build_prompt(query, contexts):
  context_text = ""
  for context in contexts:
    context_text += f"""
    File: {context['file_path']}
    Name: {context['name']}
    Type: {context['type']}
    Lines: {context['start_line']}-{context['end_line']}

    Code:
    {context['content']}
    ----------------------------------------
    """

    prompt = f"""
    You are an AI code assistant.
    Answer ONLY using the provided repository context.
    
    Repository Context:
    {context_text}

    User Question:
    {query}

    Answer:
    """

    return prompt