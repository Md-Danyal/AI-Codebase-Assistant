from groq import Groq
import os

client = Groq(api_key = os.getenv("GROQ_API"))

def ask_llm(prompt):

  response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
      {
        "role": "user",
        "content": prompt
        }
      ]
    )

  print(response.choices[0].message.content)
  return response.choices[0].message.content