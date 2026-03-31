from basic_ops import add, subtract, multiply, divide, sine, cosine, tangent


def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def read_number(prompt):
    while True:
        raw = input(prompt).strip()

        try:
            return float(raw)
        except ValueError:
            print("Invalid input: please enter a real number.")


def handle_binary_operation(history):
    print("Available operators: +  -  *  /")
    operator = input("Enter operator: ").strip()

    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operation.")
        return

    a = read_number("Enter first number: ")
    b = read_number("Enter second number: ")

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    else:
        result = divide(a, b)
        if result is None:
            print("Error: division by zero.")
            return

    operation_text = f"{format_result(a)} {operator} {format_result(b)} = {format_result(result)}"
    history.append(operation_text)
    print("Result:", format_result(result))


def handle_scientific_operation(history):
    print("Available functions: sin  cos  tan")
    func = input("Enter function: ").strip().lower()

    if func not in ["sin", "cos", "tan"]:
        print("Invalid scientific function.")
        return

    x = read_number("Enter value (in radians): ")

    if func == "sin":
        result = sine(x)
    elif func == "cos":
        result = cosine(x)
    else:
        result = tangent(x)

    operation_text = f"{func}({format_result(x)}) = {format_result(result)}"
    history.append(operation_text)
    print("Result:", format_result(result))


def show_history(history):
    if not history:
        print("History is empty.")
        return

    print("\nOperation history:")
    for i, item in enumerate(history, start=1):
        print(f"{i}. {item}")
    print()


def main():
    history = []

    while True:
        print("\n=== Calculator Menu ===")
        print("1. Basic arithmetic operations")
        print("2. Scientific functions")
        print("3. Show history")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            handle_binary_operation(history)
        elif choice == "2":
            handle_scientific_operation(history)
        elif choice == "3":
            show_history(history)
        elif choice == "4":
            print("Exiting calculator.")
            break
        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()