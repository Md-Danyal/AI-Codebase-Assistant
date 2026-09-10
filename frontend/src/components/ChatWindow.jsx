import { useState } from "react";
import { sendQuery } from "../services/api";
import MarkdownMessage from "./MarkdownMessage";

function ChatWindow({ repoName, conversationId }) {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();

    if (!query.trim() || !repoName) {
      return;
    }

    const userMessage = {
      role: "user",
      content: query,
    };

    setMessages((previousMessages) => [...previousMessages, userMessage]);

    setQuery("");
    setLoading(true);

    try {
      const data = await sendQuery(conversationId, repoName, query);

      const aiMessage = {
        role: "assistant",
        content: data.answer,
        references: data.references,
      };

      setMessages((previousMessages) => [...previousMessages, aiMessage]);
    } catch (error) {
      const errorMessage = {
        role: "error",
        content: error.message,
      };

      setMessages((previousMessages) => [...previousMessages, errorMessage]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="chat-window">
      <div className="chat-header">
        <h2>Codebase Chat</h2>

        <span>
          {repoName
            ? `Currently chatting with ${repoName}`
            : "Index a repository to start chatting"}
        </span>
      </div>

      <div className="messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <h3>👋 Welcome!</h3>

            <p>
              {repoName
                ? `Ask anything about ${repoName}`
                : "Index a GitHub repository first."}
            </p>
          </div>
        ) : (
          messages.map((message, index) => (
            <div key={index} className={`message ${message.role}`}>
              <span className="message-avatar">
                {message.role === "user" ? "👤" : "🤖"}
              </span>
              <strong>{message.role === "user" ? "You" : "AI"}</strong>

              <MarkdownMessage content={message.content} />
            </div>
          ))
        )}

        {loading && (
          <div className="message assistant">
            <strong>AI</strong>
            <p>Thinking...</p>
          </div>
        )}
      </div>

      <form className="chat-input" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder={
            repoName
              ? "Ask something about your code..."
              : "Index a repository first..."
          }
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          disabled={!repoName || loading}
        />

        <button type="submit" disabled={!repoName || loading}>
          {loading ? "..." : "Send"}
        </button>
      </form>
    </section>
  );
}

export default ChatWindow;
