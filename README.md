# AI Research Knowledge Agent

The `ai-research-knowledge-agent` is a Python-based application designed to process information, maintain context, and execute research tasks using a modular architecture and built-in tools.

## Architecture and Modules

The core application resides in the `app/` directory, which is divided into several specialized modules:

* **`main.py`**: Serves as the primary entry point to initialize and run the application.


* **`agent.py`**: Orchestrates model responses, tool execution, and in-process conversation history.


* **`planner.py`**: Sends the conversation to the language model and exposes the available tool definitions.


* **`memory.py`**: Manages the agent's memory and state.


* **`knowledge_base.py`**: Stores and retrieves processed research data.


* **`response_generator.py`**: Constructs the final synthesized responses delivered by the agent.


* **`tool_manager.py`**: Oversees the registration, coordination, and routing of the agent's utilities.

* **`llm_client.py`**: Configures the OpenAI-compatible client using environment variables.



## Available Tools

The agent utilizes a dedicated `app/tools/` directory containing specific utilities it can invoke during the research process:

* **Web Search (`web_search.py`)**: Enables the agent to gather external information.


* **PDF Reader (`pdf_reader.py`)**: Allows the agent to parse and extract content from PDF documents.


* **Calculator (`calculator.py`)**: Provides the agent with mathematical calculation capabilities.

## Run the agent

The agent uses OpenAI-compatible chat completions and tool calling. Install its
dependencies, set an API key, and start the command-line interface:

```powershell
pip install -r requirements.txt
$env:OPENAI_API_KEY = "your-api-key"
python app\main.py
```

The default model is `gpt-4o-mini`. Set `OPENAI_MODEL` to use another model
that supports tool calling. For an OpenAI-compatible endpoint, optionally set
`OPENAI_BASE_URL` as well. The conversation is kept in memory for the duration
of the process; type `exit` to quit.
