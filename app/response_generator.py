def generate_response(intent):
    if intent == "greeting":
        return "Hello! I am your AI Research Agent."

    if intent == "calculator":
        return "I will use the Calculator Tool."

    if intent == "web_search":
        return "I will use the Web Search Tool."

    if intent == "pdf_reader":
        return "I will use the PDF Reader Tool."

    return "I don't know how to handle that yet."