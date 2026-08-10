from planner import plan
from tool_manager import execute_tool
from response_generator import generate_response


def run_agent(user_input):
    decision = plan(user_input)

    if decision["type"] == "tool":
        result = execute_tool(
            decision["tool"],
            expression=decision["expression"]
        )

        return f"The result is {result}"

    return generate_response(decision["intent"])