from basic_ops import add, subtraction, product, division

def main():
    result = 0

    while True:
        try:
            op = input("Enter operation (+, -, *, /) or 'q' to quit: ")

            if op == 'q':
                break

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtraction(a, b)
            elif op == '*':
                result = product(a, b)
            elif op == '/':
                result = division(a, b)
                if result is None:
                    print("Error: division by zero")
                    continue
            else:
                print("Invalid operator")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input, please enter numbers")

if __name__ == "__main__":
    main()