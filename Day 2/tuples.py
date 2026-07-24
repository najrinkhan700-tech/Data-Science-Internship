name = ("Rahul", "Shivani", "Sonu", "sanjay", "Neha", True, 2.34, 23)
print(name)
print(name[6])
print(name[:])
print(name[3:])
print(name[-6])
print(name[:6])

lname = list(name)
lname.append("Rupali")
lname.insert(3,"Nazzu")
lname.extend("Dimple")
name = tuple(lname)
print(name)

print(len(name))

#remove method
lname = list(name)
lname.remove("Neha")
lname.pop(1)
del lname[0]
name = tuple(lname)
print(name)

#loop in tuple
for x in name:
    print(x)

for i in range(len(name)):
    print(name[i])

#join method
mytuple = name*2
print(mytuple)

# return numbers of occur
print(name.count("Sonu"))

# return position
print(name.index("Rupali"))

del mytuple



