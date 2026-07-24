"""
Data type
Numeric Data type:
int - Integer, 121,12,9,79,0,35,-12
float- decimal values, 23.3,5.2

complex data type
ex 2x+4y,3t+4

text data type:
string- sequence of alpha numeric or special characters enclosed in "", or ''
ex -
name = "Sachin@123+/.,"

boolean data type:
True, 1
False,0

set data type:
s = {10,20,30}

sequence Data type:
list,tuple,range(start,stop-1,step)

none type
None

mapping; 
dictonary
{key:value};  name = Ravi


type() - used to check type of data
"""
name = "sachin@123+/.,"
print(name)
print(type(name))

lst = [1,2,3,4]
print(lst)
print(type(lst))

num = 100.0
print(num)
print(type(num))

name = ("Ajay","Rahul","Rohit")
print(name)
print(type(name))


student = {
    "Name" : "Sachin",
    "rollno" : 1031,
    "college" : "Mpct"
}

print(student)
print(type(student))

