from tokens import Number, Operator


def tokenize(expr):
    expr = expr.replace(" ", "")
    if not expr:
        return None, "Empty input"

    tokens = []
    i = 0
    expect_number = True

    while i < len(expr):
        ch = expr[i]

        if expect_number:
            sign = 1

            if ch == '-':
                sign = -1
                i += 1
                if i >= len(expr):
                    return None, "Invalid expression"

            start = i
            dot_count = 0

            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                if expr[i] == '.':
                    dot_count += 1
                    if dot_count > 1:
                        return None, "Invalid number"
                i += 1

            if start == i:
                return None, "Expected number"

            number_str = expr[start:i]
            try:
                value = sign * float(number_str)
            except ValueError:
                return None, "Invalid number"

            tokens.append(Number(value))
            expect_number = False

        else:
            if ch not in '+-*/':
                return None, "Expected operator"

            tokens.append(Operator(ch))
            i += 1
            expect_number = True

    if expect_number:
        return None, "Expression cannot end with an operator"

    return tokens, None


def reduce_once(values, operators, index):
    left = values[index]
    right = values[index + 1]
    op = operators[index]

    result = op.apply(left, right)
    if result is None and op.symbol == '/':
        return False, "Error: division by zero"

    values[index] = result
    del values[index + 1]
    del operators[index]
    return True, None


def evaluate(tokens):
    values = []
    operators = []

    for token in tokens:
        if isinstance(token, Number):
            values.append(token.value)
        elif isinstance(token, Operator):
            operators.append(token)

    i = 0
    while i < len(operators):
        if operators[i].symbol in '*/':
            ok, error = reduce_once(values, operators, i)
            if not ok:
                return None, error
        else:
            i += 1

    i = 0
    while i < len(operators):
        ok, error = reduce_once(values, operators, i)
        if not ok:
            return None, error

    if len(values) != 1:
        return None, "Invalid expression"

    return values[0], None


def format_result(result):
    if result.is_integer():
        return str(int(result))
    return str(result)


def main():
    while True:
        expr = input("Enter expression (or q to quit): ")

        if expr.lower() == 'q':
            break

        tokens, error = tokenize(expr)
        if error:
            print(error)
            continue

        result, error = evaluate(tokens)
        if error:
            print(error)
            continue

        print(format_result(result))


if __name__ == "__main__":
    main()