def validate_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Invalid input,expected a number.")

def add(a, b):
    validate_number(a)
    validate_number(b)
    return a + b

def subtract(a, b):
    validate_number(a)
    validate_number(b)
    return a - b

def multiply(a, b):
    validate_number(a)
    validate_number(b)
    return a * b

def divide(a, b):
    validate_number(a)
    validate_number(b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
