from basic_ops import add, subtraction, product, division


class Number:
    def __init__(self, value):
        self.value = float(value)

    def __repr__(self):
        return f"Number({self.value})"


class Operator:
    PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    def __init__(self, symbol):
        if symbol not in self.PRECEDENCE:
            raise ValueError(f"Invalid operator: {symbol}")
        self.symbol = symbol
        self.precedence = self.PRECEDENCE[symbol]

    def apply(self, left, right):
        if self.symbol == '+':
            return add(left, right)
        if self.symbol == '-':
            return subtraction(left, right)
        if self.symbol == '*':
            return product(left, right)
        if self.symbol == '/':
            return division(left, right)
        return None

    def __repr__(self):
        return f"Operator('{self.symbol}')"