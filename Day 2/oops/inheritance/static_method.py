class Employee:
    comapany = "Gwalior"
    def item(self,a):
        print(f"Hello, {self.comapany} ITM Gwalior{a}")
    
    @staticmethod
    def RJIT(a):
        print(a)

rohit = Employee()
rohit.item("Delhi")
rohit.RJIT("Ram")