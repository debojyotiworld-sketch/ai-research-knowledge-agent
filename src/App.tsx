import React from "react";
import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch("/api/research", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
    });
    const data = await response.json();
    setResult(data.result);
  };

  return (
    <div>
      <h1>AI Research Agent</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your research query"
        />
        <button type="submit">Submit</button>
      </form>
      {result && (
        <div>
          <h2>Research Result:</h2>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default App;