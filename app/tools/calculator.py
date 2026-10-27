import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def calculate(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        return _evaluate(tree.body)
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except (SyntaxError, ValueError, TypeError):
        return "Invalid expression."


def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)

    raise ValueError("Unsupported expression.")