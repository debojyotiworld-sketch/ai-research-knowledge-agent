import os

from llm_client import create_chat_completion


SYSTEM_PROMPT = (
    "You are an AI research assistant. Answer helpfully and accurately. "
    "Use the calculator for arithmetic, the web search tool for current or "
    "external information, and the PDF reader when the user provides a PDF "
    "file path. Do not claim to have used a tool unless you called it."
)

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a basic arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "An arithmetic expression such as 12 * 4.",
                    }
                },
                "required": ["expression"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for relevant information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query."}
                },
                "required": ["query"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "pdf_reader",
            "description": "Extract the text from a PDF file at a supplied path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the PDF file.",
                    }
                },
                "required": ["file_path"],
                "additionalProperties": False,
            },
        },
    },
]


def plan(messages):
    return create_chat_completion(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=messages,
        tools=TOOLS,
    )
