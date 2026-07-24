# dictonary are unorderd, not duplicate keys, Changeble
#  store the in keys and values pairs

student  = {
    "stu_id" : 1,
    "Name" : "Ajay",
    "course" : "Python"
}

print(student)
print(type(student))

print(student.get("Name"))  # Access  item 
print(student.get("course"))
print(student.get("stu_id"))


print(len(student))

# Access all items of dictonary
print(student.items())

# Access keys
print(student.keys())

# change item 
student["course"] = "Java"
print(student.get("course"))

# add item
student["College"] = "RNS"
print(student.get("College"))
print(student)
