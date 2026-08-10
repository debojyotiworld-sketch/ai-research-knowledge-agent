from tools.calculator import calculate


def execute_tool(tool_name, **kwargs):
    if tool_name == "calculator":
        return calculate(**kwargs)

    return "Tool not found."