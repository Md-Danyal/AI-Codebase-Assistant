import { useState } from "react";
import { ingestRepository } from "../services/api";

function RepositoryInput({ onRepositoryIndexed }) {
  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  function handleChange(event) {
    setRepoUrl(event.target.value);
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (!repoUrl.trim()) {
      setError("Please enter a GitHub repository URL.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const data = await ingestRepository(repoUrl);

      console.log("Ingestion response:", data);

      onRepositoryIndexed(data);
    } catch (error) {
      console.error(error);

      setError(error.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="repository-section">
      <h2>Add GitHub Repository</h2>

      <p>Enter a GitHub repository URL to index its codebase.</p>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="https://github.com/user/repository"
          value={repoUrl}
          onChange={handleChange}
          disabled={loading}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Indexing..." : "Index Repository"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}
    </section>
  );
}

export default RepositoryInput;
