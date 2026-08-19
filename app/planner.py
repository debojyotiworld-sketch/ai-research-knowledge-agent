def plan(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return {
            "type": "response",
            "intent": "greeting"
        }

    if user_input.startswith("calculate"):
        expression = user_input.replace("calculate", "").strip()

        return {
            "type": "tool",
            "tool": "calculator",
            "expression": expression
        }

    if user_input.startswith("search"):
        query = user_input.replace("search", "").strip()

        return {
            "type": "tool",
            "tool": "web_search",
            "expression": query
        }

    if user_input.startswith("read pdf"):
        file_path = user_input.replace("read pdf", "").strip()

        return {
            "type": "tool",
            "tool": "pdf_reader",
            "file_path": file_path
        }

    return {
        "type": "response",
        "intent": "unknown"
    }