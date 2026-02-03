import { useEffect, useState } from "react";

function Comment({ comment }) {
  return (
    <div style={{ marginLeft: 20 }}>
      <p>{comment.content}</p>
      {comment.replies.map(r => <Comment key={r.id} comment={r} />)}
    </div>
  );
}

function App() {
  const [posts, setPosts] = useState([]);
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/feed/").then(r => r.json()).then(setPosts);
    fetch("http://localhost:8000/leaderboard/").then(r => r.json()).then(setLeaders);
  }, []);

  return (
    <div>
      <h1>Community Feed</h1>
      {posts.map(p => (
        <div key={p.id}>
          <p>{p.content}</p>
          {p.comments.map(c => <Comment key={c.id} comment={c} />)}
        </div>
      ))}

      <h2>Leaderboard</h2>
      {leaders.map(l => <p key={l.user__username}>{l.user__username} - {l.total_karma}</p>)}
    </div>
  );
}

export default App;
