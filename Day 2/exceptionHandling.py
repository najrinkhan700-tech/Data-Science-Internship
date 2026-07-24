# print(10/0)  zero division error
# print(10/"ten") type error
# a = int(input("Enter a number::"))    value error
# print(a)

# try:
    # risky Code
# except 
    # handle exception
# else:
    # WHEN DOES OCCUR ERROR

# Finally:
    # always execute part

try:
    with open("SaloniAndAbhisek/FileHandling/xyz.txt","r") as f:
        data = f.read()
        
except FileNotFoundError:
    with open("SaloniAndAbhisek/FileHandling/affy.txt",'r') as f:
        print(f.read())
else:
    print(data)
    
finally:
    print("Execution completed")