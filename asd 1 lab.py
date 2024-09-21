class Stack:
    def __init__(self):
        self.items = []
        print("Стек создан")

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Стек пуст")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __del__(self):
        self.items.clear()
        print("Стек удален")


class Operation:
    def __init__(self, symbol, func):
        self.symbol = symbol
        self.func = func
        print(f"Операция '{symbol}' создана")

    def execute(self, a, b):
        return self.func(a, b)

    def __del__(self):
        print(f"Операция '{self.symbol}' удалена")


class Addition(Operation):
    def __init__(self):
        super().__init__('+', lambda a, b: a + b)


class Subtraction(Operation):
    def __init__(self):
        super().__init__('-', lambda a, b: a - b)


class Multiplication(Operation):
    def __init__(self):
        super().__init__('*', lambda a, b: a * b)


class Division(Operation):
    def __init__(self):
        super().__init__('/', lambda a, b: a / b)


def evaluate_polish_notation(expression):
    stack = Stack()
    operations = {
        '+': Addition(),
        '-': Subtraction(),
        '*': Multiplication(),
        '/': Division(),
    }
    
    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(int(token))
        elif token in operations:
            b = stack.pop()
            a = stack.pop()
            result = operations[token].execute(a, b)
            stack.push(result)
        else:
            raise ValueError(f"Неизвестный токен: {token}")
    
    result = stack.pop()
    del stack
    for op in operations.values():
        del op
    return result

# Пример использования
expression = "3 4 + 5 2 - * 7 /"
result = evaluate_polish_notation(expression)
print(result)  # Вывод: 3