import logging

def add(a, b):
    logging.warning(f"add: {a}, {b}")
    return a + b

def subtract(a, b):
    logging.warning(f"subtract: {a}, {b}")
    return a - b

def multiply(a, b):
    logging.warning(f"multiply: {a}, {b}")
    return a * b

if __name__ == "__main__":
    add(10, 5)
    subtract(10, 5)
    multiply(10, 5)