def evaluate_polish_notation(expression):
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    
    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        elif token in operators:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
        else:
            raise ValueError(f"Неизвестный токен: {token}")
    
    return stack.pop()

# Пример использования
expression = "3 4 + 5 2 - * 7 /"
result = evaluate_polish_notation(expression)
print(result)  # Вывод: 35