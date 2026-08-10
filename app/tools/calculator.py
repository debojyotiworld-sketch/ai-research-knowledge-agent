def calculate(expression):
    parts = expression.split()

    a = float(parts[0])
    operator = parts[1]
    b = float(parts[2])

    if operator == "+":
        return a + b

    if operator == "-":
        return a - b

    if operator == "*":
        return a * b

    if operator == "/":
        if b == 0:
            return "Cannot divide by zero."

        return a / b

    return "Unknown operator."