def generate_response(intent):
    if intent == "greeting":
        return "Hello! I am your AI Research Agent."

    if intent == "calculator":
        return "I will use the Calculator Tool."

    return "I don't know how to handle that yet."