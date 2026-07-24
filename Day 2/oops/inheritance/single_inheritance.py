class Papa:
    bike = "007"
    def showDetails(self):
        print("This is an employee")
    
class son(Papa):
    language = "Python"
    bike = "008"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        
        print("This is an programmer")
    
   

p = son()
print(p.bike)
p.showDetails()
p.getLanguage()