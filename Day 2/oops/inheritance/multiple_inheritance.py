class Employee:
    car = "pnInfosys"
    ecode = 120

class Freelancer:
    car = "Google"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
        return super().__class__car

class programmer(Employee, Freelancer):
    # car = "abcd"
    name = "Vikas"


p = programmer()
print(p.car)
p.upgradeLevel()
print(p.level)