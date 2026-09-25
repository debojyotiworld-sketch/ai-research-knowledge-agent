# AI Research Knowledge Agent

The `ai-research-knowledge-agent` is a Python-based application designed to process information, maintain context, and execute research tasks using a modular architecture and built-in tools.

## Architecture and Modules

The core application resides in the `app/` directory, which is divided into several specialized modules:

* **`main.py`**: Serves as the primary entry point to initialize and run the application.


* **`agent.py`**: Contains the core agent logic and orchestration.


* **`planner.py`**: Responsible for breaking down complex queries and creating task execution strategies.


* **`memory.py`**: Manages the agent's memory and state.


* **`knowledge_base.py`**: Stores and retrieves processed research data.


* **`response_generator.py`**: Constructs the final synthesized responses delivered by the agent.


* **`tool_manager.py`**: Oversees the registration, coordination, and routing of the agent's utilities.



## Available Tools

The agent utilizes a dedicated `app/tools/` directory containing specific utilities it can invoke during the research process:

* **Web Search (`web_search.py`)**: Enables the agent to gather external information.


* **PDF Reader (`pdf_reader.py`)**: Allows the agent to parse and extract content from PDF documents.


* **Calculator (`calculator.py`)**: Provides the agent with mathematical calculation capabilities.
