num1 = float(input("Enter first number :"))   
num2 = float(input("Enter second number :"))   
res = None
opt = input('Enter your operation (+, -, *, /) :')

if opt == '+':
    res = num1 + num2
    print(f'Addition: {num1} + {num2} = {res}')
elif opt == '-':
    res = num1 - num2
    print(f'Subtraction: {num1} - {num2} = {res}')
elif opt == '*':
    res = num1 * num2
    print(f'Multiplication: {num1} * {num2} = {res}')
elif opt == '/':
    if num2 != 0:
        res = num1 / num2
        print(f'Division : {num1} / {num2} = {res}') 
    else:
        print('Error!, Division by zero.')

else:
    print("Enter valid operation.")

    