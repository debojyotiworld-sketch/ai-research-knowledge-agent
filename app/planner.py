def plan(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "greeting"

    if user_input.startswith("calculate"):
        return "calculator"

    return "unknown"