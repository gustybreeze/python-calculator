class Calc:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.opr = ""

    def opt(self):
        self.opr = input("Enter your operation (=, -, *, /, %, **) : ")
       

    def num(self):
        self.a = float(input("Enter first number :"))
        self.b = float(input("Enter second number :"))

    def calculate(self):
        if self.opr == '+':
            return self.a + self.b
        elif self.opr == '-':
            return self.a - self.b
        elif self.opr == '*':
            return self.a * self.b
        elif self.opr == '/':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error!: Division by zero."
        elif self.opr == '%':
            if self.b != 0:
                return self.a % self.b
            else:
                return "Error!: Division by zero."
        elif self.opr == '**':
            return self.a ** self.b
        else:
            return "Invalid operation."
        
    
c = Calc()
c.num()
c.opt()
res = c.calculate()
print("Result", res) 