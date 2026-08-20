from planner import plan
from tool_manager import execute_tool
from response_generator import generate_response


def run_agent(user_input):
    decision = plan(user_input)

    if decision["type"] == "tool":
        if decision["tool"] == "pdf_reader":
            result = execute_tool(
                decision["tool"],
                file_path=decision["file_path"]
            )
            
            return f"The content of the PDF is:\n{result}"
        
        result = execute_tool(
            decision["tool"],
            expression=decision["expression"]
        )

        return f"The result is {result}"

    return generate_response(decision["intent"])