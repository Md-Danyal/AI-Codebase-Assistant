from groq import Groq
# import os
from backend.app.config import settings

# client = Groq(api_key = os.getenv("GROQ_API"))
client = Groq(api_key = settings.GROQ_API_KEY)

def ask_llm(prompt):

  responses = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": prompt
        }
      ],
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
    )

  # print(response)
  # return response.choices[0].message.content
  
  # for response in responses:
  #   print(response.choices[0].delta.content or "", end="")
  
  answer = ""

  for response in responses:
    answer += response.choices[0].delta.content or ""

  return answer