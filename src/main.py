import re
from basic_ops import add, subtraction, product, division


def tokenize(expr):
    expr = expr.replace(" ", "")
    pattern = r'\d+(?:\.\d+)?|[+\-*/]'
    tokens = re.findall(pattern, expr)

    # controllo semplice: i token ricostruiti devono coincidere con l'input
    if ''.join(tokens) != expr:
        return None

    return tokens


def apply_operator(a, op, b):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtraction(a, b)
    elif op == '*':
        return product(a, b)
    elif op == '/':
        return division(a, b)
    return None


def evaluate_expression(tokens):
    if not tokens or len(tokens) % 2 == 0:
        return None, "Invalid expression"

    # i numeri devono stare in posizione pari, gli operatori in posizione dispari
    for i in range(0, len(tokens), 2):
        try:
            tokens[i] = float(tokens[i])
        except ValueError:
            return None, "Invalid number"

    for i in range(1, len(tokens), 2):
        if tokens[i] not in ['+', '-', '*', '/']:
            return None, "Invalid operator"

    # prima passata: * e /
    values = [tokens[0]]
    ops = []

    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = tokens[i + 1]

        if op in ['*', '/']:
            left = values.pop()
            result = apply_operator(left, op, num)
            if result is None and op == '/':
                return None, "Error: division by zero"
            values.append(result)
        else:
            ops.append(op)
            values.append(num)

        i += 2

    # seconda passata: + e -
    result = values[0]
    for i in range(len(ops)):
        result = apply_operator(result, ops[i], values[i + 1])

    return result, None


def main():
    while True:
        expr = input("Enter expression (or q to quit): ")

        if expr.lower() == 'q':
            break

        tokens = tokenize(expr)
        if tokens is None:
            print("Invalid input")
            continue

        result, error = evaluate_expression(tokens)

        if error:
            print(error)
        else:
            # stampa più pulita: 6 invece di 6.0 quando possibile
            if result.is_integer():
                print(int(result))
            else:
                print(result)


if __name__ == "__main__":
    main()