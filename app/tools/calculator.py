def calculate(a, b, operation):
    if operation == 'add':
        return a + b

    if operation == 'subtract':
        return a - b

    if operation == 'multiply':
        return a * b

    if operation == 'divide':
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    
    return "Error: Invalid operation."