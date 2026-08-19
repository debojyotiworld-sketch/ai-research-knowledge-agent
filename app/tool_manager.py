from tools.calculator import calculate
from tools.pdf_reader import read_pdf

def execute_tool(tool_name, **kwargs):
    if tool_name == "calculator":
        return calculate(**kwargs)
    elif tool_name == "pdf_reader":
        return read_pdf(**kwargs)

    return "Tool not found."