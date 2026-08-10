def plan(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return {
            "type": "response",
            "intent": "greeting"
        }

    if user_input.startswith("calculate"):
        return {
            "type": "tool",
            "tool": "calculator"
        }

    return {
        "type": "response",
        "intent": "unknown"
    }