class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def result(self):
        if self.marks >= 40:
            print(self.name,"Pass")
        else:
            print(self.name,"Fail")
s1 = Student("Rahul",90)
s2 = Student("Sonu",37)
s1.result()
s2.result()