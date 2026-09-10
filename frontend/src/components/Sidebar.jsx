function Sidebar({ repoName }) {
  return (
    <aside className="sidebar">
      <button className="new-chat">+ New Chat</button>

      <div className="sidebar-section">
        <h3>Repository</h3>

        {repoName ? (
          <div className="repo-placeholder">📁 {repoName}</div>
        ) : (
          <div className="repo-placeholder">No repository selected</div>
        )}
      </div>

      <div className="sidebar-section">
        <h3>Conversations</h3>

        <p className="empty-text">No conversations yet</p>
      </div>
    </aside>
  );
}

export default Sidebar;
