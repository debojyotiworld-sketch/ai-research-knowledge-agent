import { useState } from 'react'
import './App.css'

function App() {
  const [query, setQuery] = useState('')

  const handleResearch = () => {
    if (!query.trim()) return

    console.log('Research query:', query)
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