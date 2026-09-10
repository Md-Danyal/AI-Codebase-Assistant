import { useState } from "react";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import RepositoryInput from "./components/RepositoryInput";
import ChatWindow from "./components/ChatWindow";

function App() {
  const [repoName, setRepoName] = useState("");
  const [repositoryInfo, setRepositoryInfo] = useState(null);

  const [conversationId, setConversationId] = useState(crypto.randomUUID());

  function handleRepositoryIndexed(data) {
    const name = data.repository.repo_name;

    setRepoName(name);
    setRepositoryInfo(data);
  }

  return (
    <div className="app">
      <Navbar />

      <div className="main-layout">
        <Sidebar repoName={repoName} />

        <main className="content">
          <RepositoryInput onRepositoryIndexed={handleRepositoryIndexed} />

          <ChatWindow repoName={repoName} conversationId={conversationId} />
        </main>
      </div>
    </div>
  );
}

export default App;
