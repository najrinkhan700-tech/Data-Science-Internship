class Employee:
    name = "Vikas"
    _company = "pnInfosys"
    __salary = 100000

    def display(self):
        print(self.__salary)

e1 = Employee()
print(e1.name)
print(e1._company)
print(e1.__salary)