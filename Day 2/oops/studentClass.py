class Student:
    def __init__(self,name,marks,password):
        self.name = name
        self._marks = marks
        self.__password = password

    def display(self):
        print("Name:",self.name)
        print("Marks:",self._marks)
    
    def __check_password(self):
        print("Password:",self.__password)
    
    def log_in(self):
        self.__check_password()
    
class Result(Student):
    def grade(self):
        if self._marks >= 75:
            print("Grade : A")

        elif self._marks >= 55:
            print("Grade : B")

        elif self._marks >= 40:
            print("Grade : c")

        elif self._marks >= 34:
            print("Grade : D")
        
        else:
            print("Fail")

# object creation 
s1 = Result("Rahul",0,"1234")
s1.display()
s1.log_in()
s1.grade()