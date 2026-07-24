class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def Add(self):
        print("Addition:",self.a + self.b)

    def Sub(self):
        print("Substraction:",self.a - self.b)

    def mul(self):
        print("Multiplication:",self.a * self.b)

    def div(self):
        print("Division:",self.a / self.b)
    def rem(self):
        print("Reminder:",self.a % self.b)

s = calculator(10,20)
s.Add()
s.Sub()
s.mul()
s.div()
s.rem()