def generate_response(message):
    if not message.content:
        raise RuntimeError("The model returned no response text.")
    return message.content
