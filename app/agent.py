from planner import plan
from response_generator import generate_response


def run_agent(user_input):
    intent = plan(user_input)

    response = generate_response(intent)

    return response