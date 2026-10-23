def evaluate_postfix(z):
    stack = []

    for ch in z:
        if ch.isdigit():
            stack.append(int(ch))          # operand -> push
        else:
            b = stack.pop()                # pehle right operand
            a = stack.pop()                # phir left operand
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
            elif ch == '^':
                stack.append(a ** b)

    return stack.pop()

print(evaluate_postfix("23*54*+9-"))   # 17

#___________________________________________________________________________________________________

