import json
import redis

from backend.app.config import settings


redis_client = redis.from_url(
  settings.REDIS_URL,
  decode_responses=True
)


def get_memory_key(conversation_id: str) -> str:
  return f"conversation:{conversation_id}"

def get_conversation(conversation_id: str) -> list:
  key = get_memory_key(conversation_id)
  messages = redis_client.lrange(key, 0, -1)
  return [json.loads(message) for message in messages]

def add_message(conversation_id: str, role: str, content: str):
  key = get_memory_key(conversation_id)
  message = {
    "role": role,
    "content": content
  }
  redis_client.rpush(
    key,
    json.dumps(message)
  )

def clear_conversation(conversation_id: str):
  key = get_memory_key(conversation_id)
  redis_client.delete(key)