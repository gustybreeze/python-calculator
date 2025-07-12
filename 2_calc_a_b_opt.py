''' ------- STRUCTURE THE CODE USING A FUNCTION ------- '''
def calc(a, b, operator):
    try:
        if operator == '+':
            return f'{a} + {b} = {a + b}'
        elif operator == '-':
            return f'{a} - {b} = {a - b}'
        elif operator == '*':
            return f'{a} * {b} = {a * b}'
        elif operator == '/':
            return f'{a} / {b} = {a / b}'
        else:
            return 'Invalid operator.'
    
    except ZeroDivisionError:
        return 'Error! Division by zero.'
    
    except Exception as e:
        return f'Unexpected error : {e}'
    
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter your operation (+, -, *, /, %, **): ").strip()

    result = calc(num1, num2, op)
    print(result)
except ValueError:
    print("Invalid input. Please enter numeric values only.")
