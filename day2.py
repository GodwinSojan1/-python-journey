a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = input('select the operation (+,-,/,*): ')

if c == '+':
    print(f"{a} + {b} = {a + b}")
elif c == '-':
    print(f"{a} - {b} = {a - b}")
elif c == '*':
    print(f"{a} * {b} = {a * b}")
elif c == '/':
    print(f"{a} / {b} = {a / b}")
else:
    print('Invalid operator!')