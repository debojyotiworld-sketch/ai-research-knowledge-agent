import { useState } from 'react'
import './App.css'

function App() {
  const [query, setQuery] = useState('')

  const handleResearch = () => {
    if (!query.trim()) return

    // POST request to the backend API with the research query
    fetch('http://localhost:5000/research', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response data from the backend
        console.log('Research results:', data)
      })
      .catch((error) => {
        console.error('Error during research:', error)
      })
  }

  return (
    <main className="app">
      <section className="research-container">
        <div className="hero">
          
          <p className="eyebrow">AI RESEARCH ASSISTANT</p>

          <h1>What would you like to research?</h1>

          <p className="description">
            Ask a question and let the AI help you research the topic.
          </p>
        </div>

        <div className="research-box">
          <textarea
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Ask anything..."
            rows={5}
          />

          <button
            type="button"
            onClick={handleResearch}
            disabled={!query.trim()}
          >
            Start Research
          </button>
        </div>
      </section>
    </main>
  )
}

export default App