import os


_client = None


def get_client():
    global _client

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Set it in your environment before "
            "starting the AI Research Agent."
        )

    if _client is None:
        try:
            from openai import OpenAI
        except ImportError as error:
            raise RuntimeError(
                "The OpenAI Python package is missing. Install dependencies "
                "with 'pip install -r requirements.txt'."
            ) from error

        client_options = {"api_key": api_key}
        base_url = os.getenv("OPENAI_BASE_URL")
        if base_url:
            client_options["base_url"] = base_url
        _client = OpenAI(**client_options)

    return _client


def create_chat_completion(model, messages, tools=None):
    request = {"model": model, "messages": messages}
    if tools:
        request["tools"] = tools
        request["tool_choice"] = "auto"

    return get_client().chat.completions.create(**request)
