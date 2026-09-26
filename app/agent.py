import json

from app.planner import SYSTEM_PROMPT, plan
from app.response_generator import generate_response
from app.tool_manager import execute_tool


MAX_TOOL_ROUNDS = 5
_conversation = [{"role": "system", "content": SYSTEM_PROMPT}]


def reset_conversation():
    _conversation[:] = [{"role": "system", "content": SYSTEM_PROMPT}]


def run_agent(user_input):
    if not isinstance(user_input, str) or not user_input.strip():
        raise ValueError("Please enter a non-empty message.")

    _conversation.append({"role": "user", "content": user_input.strip()})

    for round_number in range(MAX_TOOL_ROUNDS + 1):
        completion = plan(_conversation)
        if not completion.choices:
            raise RuntimeError("The model returned an empty completion.")
        message = completion.choices[0].message
        tool_calls = message.tool_calls or []
        assistant_message = {"role": "assistant", "content": message.content}
        if tool_calls:
            assistant_message["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in tool_calls
            ]
        _conversation.append(assistant_message)

        if not tool_calls:
            return generate_response(message)

        if round_number == MAX_TOOL_ROUNDS:
            raise RuntimeError(
                f"The model exceeded the limit of {MAX_TOOL_ROUNDS} tool rounds."
            )

        for tool_call in tool_calls:
            arguments = json.loads(tool_call.function.arguments)
            if not isinstance(arguments, dict):
                raise ValueError("Tool arguments must be a JSON object.")

            result = execute_tool(tool_call.function.name, **arguments)
            _conversation.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result, ensure_ascii=False, default=str),
                }
            )

    raise RuntimeError("The agent could not complete the request.")