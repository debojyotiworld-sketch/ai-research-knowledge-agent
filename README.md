# 🤖 AI Research Agent

An intelligent and modular AI research assistant designed to autonomously plan, execute, and synthesize research tasks.

The project combines a **Python-based AI Agent** with a **React + TypeScript + Vite interface**. The agent is designed around specialized tools such as web search, PDF reading, and calculations, with separate modules for planning, memory, knowledge management, tool execution, and response generation.

The long-term goal is to build a full-stack AI research system that can take a complex question, determine what actions are required, use the appropriate tools, and return a synthesized research result through a web interface.

---

## ✨ Features

### 🧠 AI Agent

The AI Agent is the core of the application.

It is responsible for processing user queries and coordinating the research workflow.

The agent is designed to:

* Understand user research requests
* Plan research tasks
* Execute appropriate tools
* Process tool results
* Maintain relevant context
* Synthesize information into a final response

---

### 📋 Autonomous Planning

Complex research questions can be broken down into smaller, actionable steps.

The intended workflow is:

```text
User Query
    ↓
Understand the Request
    ↓
Create Research Plan
    ↓
Execute Required Steps
    ↓
Collect Information
    ↓
Synthesize Findings
    ↓
Final Response
```

---

### 🛠️ Tool-Based Architecture

The agent uses specialized tools to perform tasks that cannot or should not be handled by the language model alone.

Current tool categories include:

* 🌐 Web Search
* 📄 PDF / Document Reader
* 🧮 Calculator

The tool-based architecture makes the system extensible, allowing additional tools to be added later.

---

### 🧠 Memory

A dedicated memory module is included to manage conversation context and agent state.

This provides a foundation for maintaining context during longer research tasks.

---

### 📚 Knowledge Base

The project includes a knowledge-base layer for storing and retrieving research information.

This provides the foundation for future:

* Retrieval-Augmented Generation (RAG)
* Vector database integration
* Persistent research knowledge
* Document-based question answering

---

### 🔌 Modular Design

The application separates different responsibilities into independent Python modules.

This makes the system easier to:

* Understand
* Test
* Debug
* Extend
* Maintain

---

### 💻 Web Interface

The user interface is built with:

* React
* TypeScript
* Vite

The interface allows users to enter research questions and communicate with the Python AI Agent through an HTTP API.

---

# 🏗️ Architecture

The project is designed around the following architecture:

```text
┌──────────────────────────┐
│      React Frontend      │
│   React + TypeScript     │
└────────────┬─────────────┘
             │
             │ HTTP Request
             ▼
┌──────────────────────────┐
│       Python API         │
│      FastAPI Layer       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        AI Agent          │
│                          │
│ Planning & Orchestration │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      Tool Manager        │
└────────────┬─────────────┘
             │
    ┌────────┼──────────┐
    ▼        ▼          ▼
Web Search  PDF   Calculator
    │       Reader      │
    └────────┼──────────┘
             │
             ▼
┌──────────────────────────┐
│ Memory / Knowledge Base  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Response Generator    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      React Frontend      │
│      Display Result      │
└──────────────────────────┘
```

---

# 🔄 Research Workflow

A typical research request follows this general flow:

```text
User
 ↓
React Interface
 ↓
HTTP POST Request
 ↓
Python Backend API
 ↓
AI Agent
 ↓
Planner
 ↓
Tool Manager
 ↓
Specialized Tools
 ↓
Memory / Knowledge Base
 ↓
Response Generator
 ↓
Backend Response
 ↓
React Interface
 ↓
Research Result
```

For a complex research task, the agent may need to use multiple tools:

```text
Research Question
       ↓
     Planner
       ↓
   Web Search
       ↓
  Collect Data
       ↓
   Calculator
       ↓
 Verify Information
       ↓
  Synthesize Results
       ↓
  Final Response
```

---

# 📂 Project Structure

The current Python application follows a modular structure:

```text
ai-research-agent/
│
├── app/
│   ├── main.py
│   │
│   ├── agent.py
│   ├── planner.py
│   ├── memory.py
│   ├── knowledge_base.py
│   ├── response_generator.py
│   ├── tool_manager.py
│   │
│   └── tools/
│       ├── calculator.py
│       ├── pdf_reader.py
│       └── web_search.py
│
├── .gitignore
│
└── README.md
```

The React + TypeScript + Vite application is currently maintained alongside the Python application rather than inside a dedicated `frontend/` directory.

As the project grows, the application structure may be reorganized into separate client and server directories.

---

# 🧩 Core Components

## `app/main.py`

The current application entry point for interacting with the agent from the command line.

The basic flow is:

```text
User Input
    ↓
run_agent()
    ↓
Agent Response
    ↓
Terminal
```

---

## `app/agent.py`

The core agent logic and orchestration layer.

It is responsible for coordinating the research process and working with the other modules.

Conceptually:

```text
User Query
    ↓
Agent
    ↓
Planning
    ↓
Tool Execution
    ↓
Research
    ↓
Response
```

---

## `app/planner.py`

Responsible for breaking research requests into smaller tasks and creating an execution plan.

Example:

```text
"What are the effects of AI on software development?"

        ↓

1. Research current AI adoption
2. Identify major use cases
3. Analyze benefits
4. Analyze limitations
5. Synthesize findings
```

---

## `app/tool_manager.py`

Acts as the routing layer between the AI Agent and the available tools.

```text
Agent
  ↓
Tool Manager
  ├── Web Search
  ├── PDF Reader
  └── Calculator
```

This allows the agent to use different capabilities without tightly coupling the core agent logic to individual tools.

---

## `app/tools/calculator.py`

Provides mathematical calculation capabilities.

It can be used when the research process requires numerical calculations or verification.

---

## `app/tools/pdf_reader.py`

Provides document/PDF processing capabilities.

It is intended to allow the agent to extract useful information from research papers, reports, and other documents.

---

## `app/tools/web_search.py`

Provides web search capabilities for retrieving current or external information.

This is particularly useful for research questions that require information beyond the agent's existing knowledge.

---

## `app/memory.py`

Responsible for managing relevant conversation context and agent state.

The module provides a foundation for future short-term and long-term memory capabilities.

---

## `app/knowledge_base.py`

Responsible for the knowledge storage and retrieval layer.

It provides the foundation for future RAG and vector database capabilities.

---

## `app/response_generator.py`

Responsible for turning the information collected during the research process into a final response.

Conceptually:

```text
Research Findings
       ↓
Response Generator
       ↓
Structured Final Answer
```

---

# 🌐 Frontend

The web interface is built using:

* React
* TypeScript
* Vite

The current interface provides a research input where users can enter a question and start the research process.

Example:

```text
┌──────────────────────────────────────────┐
│          AI RESEARCH ASSISTANT           │
│                                          │
│ What would you like to research?         │
│                                          │
│ ┌──────────────────────────────────────┐ │
│ │ Ask anything...                      │ │
│ │                                      │ │
│ └──────────────────────────────────────┘ │
│                                          │
│           [ Start Research ]             │
└──────────────────────────────────────────┘
```

---

# 🔗 Frontend ↔ Backend Communication

The frontend communicates with the Python AI Agent through an HTTP API.

The intended request flow is:

```text
React
  │
  │ POST /research
  │
  ▼
FastAPI
  │
  │ query
  ▼
run_agent(query)
  │
  ▼
AI Research Agent
  │
  ▼
Research Result
  │
  ▼
JSON Response
  │
  ▼
React
```

Example request:

```json
{
  "query": "What are AI agents?"
}
```

Example response:

```json
{
  "answer": "..."
}
```

This separation keeps the responsibilities clear:

```text
Frontend
→ User Interface

Backend API
→ Communication Layer

AI Agent
→ Reasoning & Orchestration

Tools
→ Actual External Operations

Knowledge Base / Memory
→ Information & Context
```

---

# 🚀 Getting Started

## Prerequisites

Make sure the following are installed:

* Python 3.9+
* Node.js
* npm
* Git

You will also need API keys depending on the LLM and external services used by the project.

---

## 1. Clone the Repository

```bash
git clone https://github.com/debojyotiworld-sketch/ai-research-knowledge-agent.git

cd ai-research-agent
```

---

## 2. Create a Python Virtual Environment

### Windows

```powershell
python -m venv .venv

.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Backend Dependencies

If a `requirements.txt` file is available:

```bash
python -m pip install -r requirements.txt
```

For the API layer:

```bash
python -m pip install fastapi uvicorn
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
LLM_API_KEY=your_api_key_here
SEARCH_API_KEY=your_api_key_here
```

Never commit API keys or other secrets to GitHub.

---

# ▶️ Running the AI Agent

The current CLI interface can be started with:

```bash
python app/main.py
```

Example:

```text
AI Research Agent
Type 'exit' to quit.

You: What is an AI agent?

Agent: ...
```

---

# 🚀 Running the Backend API

The FastAPI layer exposes the agent to the web interface.

Example:

```bash
python -m uvicorn api:app --reload --port 5000
```

The API will be available at:

```text
http://localhost:5000
```

FastAPI's interactive documentation can be accessed at:

```text
http://localhost:5000/docs
```

---

# 💻 Running the React Application

From the directory containing the React/Vite application:

```bash
npm install
```

Then:

```bash
npm run dev
```

Vite will provide a local development URL, usually:

```text
http://localhost:5173
```

---

# 🧪 Development Approach

The project is being developed incrementally rather than attempting to build a fully autonomous research system at once.

The development path is:

```text
Basic Agent
    ↓
Tool Integration
    ↓
Planning
    ↓
Agent Execution Loop
    ↓
Memory
    ↓
Knowledge Base
    ↓
Backend API
    ↓
React Integration
    ↓
Full-Stack AI Research Agent
```

Each layer is developed and tested before adding the next layer.

---

# 🎯 Project Goals

The long-term goal is to build an AI research assistant capable of:

* Understanding complex research questions
* Creating multi-step research plans
* Selecting appropriate tools
* Searching the web
* Reading documents
* Performing calculations
* Verifying information
* Maintaining useful context
* Storing research knowledge
* Synthesizing findings
* Returning structured research results
* Providing the results through a web interface

---

# 🔮 Future Improvements

Planned improvements include:

* [ ] Complete frontend ↔ backend integration
* [ ] FastAPI backend
* [ ] Improved autonomous planning
* [ ] LLM-based tool selection
* [ ] Multi-step agent execution
* [ ] Persistent conversation memory
* [ ] Vector database integration
* [ ] Retrieval-Augmented Generation (RAG)
* [ ] Source tracking and citations
* [ ] Streaming responses
* [ ] Research history
* [ ] User authentication
* [ ] Automated testing
* [ ] Agent evaluation
* [ ] Production deployment

---

# 📌 Current Development Status

The project currently has the foundational AI Agent architecture and a React-based research interface.

The immediate development goal is to connect the two layers:

```text
React Interface
      ↓
POST /research
      ↓
FastAPI Backend
      ↓
run_agent(query)
      ↓
AI Agent
      ↓
Tools / Memory / Knowledge Base
      ↓
Research Result
      ↓
JSON Response
      ↓
React Interface
```

Once this connection is complete, the application will have a complete basic flow from:

**User → Frontend → Backend → AI Agent → Result → Frontend**

---

# 👨‍💻 Author

**Debojyoti**

GitHub:

https://github.com/debojyotiworld-sketch

---

# 📄 License

This project is currently under development.

License information will be added as the project matures.
