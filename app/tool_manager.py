from app.tools.calculator import calculate
from app.tools.pdf_reader import read_pdf
from app.tools.web_search import web_search


def execute_tool(tool_name, **kwargs):
    if tool_name == "calculator":
        return calculate(**kwargs)
    if tool_name == "pdf_reader":
        return read_pdf(**kwargs)
    if tool_name == "web_search":
        return web_search(**kwargs)

    raise ValueError(f"Unknown tool requested by the model: {tool_name}")