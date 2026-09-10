const API_BASE_URL = "http://localhost:8000";

export async function ingestRepository(repoUrl) {
  const response = await fetch(`${API_BASE_URL}/api/v1/repositories/ingest`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      repo_url: repoUrl,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Failed to index repository");
  }

  return data;
}

export async function sendQuery(conversationId, repoName, query) {
  const response = await fetch(`${API_BASE_URL}/api/v1/chat/query`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      conversation_id: conversationId,
      repo_name: repoName,
      query: query,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Failed to get response");
  }

  return data;
}
