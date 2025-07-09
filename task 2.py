# calculator.py

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculate(x: float, y: float, operation: str) -> float:
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation '{operation}'. Choose from +, -, *, /.")

    return operations[operation](x, y)

def main() -> None:
    print("=== Simple Calculator ===")

    while True:
        try:
            x = float(input("Enter the first number: "))
            operation = input("Enter an operation (+, -, *, /): ").strip()
            y = float(input("Enter the second number: "))

            result = calculate(x, y, operation)
            print(f"Result: {x} {operation} {y} = {result}")

        except ValueError as e:
            print(f"Error: {e}")

        again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()

