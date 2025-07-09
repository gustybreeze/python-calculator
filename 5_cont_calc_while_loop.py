while True:
    num1 = float(input("Enter first number :"))   
    num2 = float(input("Enter second number :"))   

    opt = input('Enter your operation (+, -, *, /) :')

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

    choice = input('\nDo you want to perform another calculations? (Yes/No): ').strip().lower()
    if choice in ('no', 'n', 'quit', 'exit'):
        print("Calculator closed. Goodbye!")
        break
    print('-'*40)