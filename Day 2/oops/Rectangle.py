class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def Area(self):
        print(self.length * self.width)
    
    def Perimeter(self):
        print(2 * (self.length + self.width))
    
l = float(input("Enter length of rectangle:")) 
w = float(input("Enter width of rectangle:"))

rec = Rectangle(l,w)

rec.Area()
rec.Perimeter()