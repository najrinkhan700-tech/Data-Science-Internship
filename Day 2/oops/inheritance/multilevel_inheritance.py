class Person:
    country = "India"

    def takeBreadth(self):
        print("Gwalior")

class Employee(Person):
    company = "HOnda"

    def getSalary(self):
        print("Salary 10000")
    
    def takeBreadth(self):
        return super().takeBreadth()
        print("Pninfosys")
    
class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreadth(self):
        return super().takeBreadth()
        print("I am an programmer so i am luckily breathing++... ")

p = Programmer()
p.takeBreadth()
p.getSalary()
