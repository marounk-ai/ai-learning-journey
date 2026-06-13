# calculator.py
# A simple CLI calculator with error handling
# Week 2 — AI Learning Journey

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {operator}")

def main():
    print("Simple Calculator")
    print("-" * 20)
    
    try:
        a = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ").strip()
        b = float(input("Second number: "))
        
        result = calculate(a, operator, b)
        print(f"\n{a} {operator} {b} = {result}")
        
    except ValueError as e:
        print(f"Input error: {e}")
    except ZeroDivisionError as e:
        print(f"Math error: {e}")

if __name__ == "__main__":
    main()