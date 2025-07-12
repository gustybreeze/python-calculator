''' ------- DIVISION BY ZERO USING try-except. ------- '''
try:
    num1 = float(input("Enter first number :").strip())   
    num2 = float(input("Enter second number :").strip())   

    opt = input('Enter your operation (+, -, *, /) :').strip()

    if opt == '+':
        print('Addition', num1 + num2)
    elif opt == '-':
        print('Subtraction :', num1 - num2)
    elif opt == '*':
        print('Multiplication :', num1 * num2)
    elif opt == '/':
        if num2 != 0:
            print('Division :',num1 / num2)
        else:
            print('Error!, Division by zero.')

    else:
        print("Enter valid operation.")

except ValueError:
    print('Invalid Input.')
