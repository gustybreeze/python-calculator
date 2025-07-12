''' ------- CALCULATOR APP ------- '''

class calculator:
    def __init__(self):
        self.history_file = "history.txt"

    def calculate(self, a, b, operator):
        try:
            if operator == '+':
                return a + b
            
            if operator == '-':
                return a - b
            
            if operator == '*':
                return a * b
            
            if operator == '/':
                return a / b
            
            if operator == '%':
                return a % b
            
            if operator == '**':
                return a ** b
            else:
                return "Invalid operator!"
        except ZeroDivisionError:
            return "Error : Cannot divide by zero."

    def log_history(self, expression, result):
        with open(self.history_file, "a") as f:
            f.write(f'{expression} = {result}\n')

    def display_menu(self):
        print('\nAvailable operations:')
        print(" + : Addition")
        print(" - : Subtraction")
        print(" * : Multiplication")
        print(" / : Division")
        print(" % : Modulus")
        print(" ** : Exponentiation")
        print(" q : Quit")

    def run(self):
        while True:
            self.display_menu()
            op = input("\nEnter operator (or 'q' to quit): ")    
            if op.lower() == 'q':
                print("Exiting Calculator. Goodbye!")
                break

            try:
                a = float(input("Enter first number: "))   
                b = float(input("Enter second number: "))   
            except ValueError:
                print("Please enter valid number!")
                continue

            result = self.calculate(a, b, op)
            expression = f"{a} {op} {b}"
            print(f"Result: {expression} = {result}")
            self.log_history(expression, result) 

calc = calculator()
calc.run()                

