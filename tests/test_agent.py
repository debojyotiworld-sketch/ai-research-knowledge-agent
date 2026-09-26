import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import agent


def completion(content=None, tool_calls=None):
    message = SimpleNamespace(content=content, tool_calls=tool_calls or [])
    return SimpleNamespace(choices=[SimpleNamespace(message=message)])


def tool_call(name, arguments, call_id="call-1"):
    return SimpleNamespace(
        id=call_id,
        function=SimpleNamespace(name=name, arguments=json.dumps(arguments)),
    )


class AgentTests(unittest.TestCase):
    def setUp(self):
        agent.reset_conversation()

    def test_generates_a_response_with_the_model(self):
        with patch.object(agent, "plan", return_value=completion("Hello!")):
            self.assertEqual(agent.run_agent("Hi"), "Hello!")

    def test_executes_model_selected_tool_and_sends_result_back(self):
        responses = [
            completion(tool_calls=[tool_call("calculator", {"expression": "2 + 2"})]),
            completion("2 + 2 = 4."),
        ]

        with patch.object(agent, "plan", side_effect=responses) as mock_plan:
            with patch.object(agent, "execute_tool", return_value=4) as mock_tool:
                self.assertEqual(agent.run_agent("What is 2 + 2?"), "2 + 2 = 4.")

        mock_tool.assert_called_once_with("calculator", expression="2 + 2")
        self.assertEqual(
            next(
                message["content"]
                for message in agent._conversation
                if message["role"] == "tool"
            ),
            "4",
        )

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            agent.run_agent("  ")


if __name__ == "__main__":
    unittest.main()
