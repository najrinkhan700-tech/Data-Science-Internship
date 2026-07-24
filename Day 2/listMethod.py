cities = ["Gwalior","Indore","Bhopal","Mumbai","Nasik","Pune","Chennai","Goa","Jabalpur"]

# append(val)
cities.append(89)
print(cities)

# insert(idx,val)
cities.insert(1,"Banglore")
print(cities)

# extend()
cities.extend([1,2,3])
print(cities)

cities.extend("Hello")
print(cities)

# pop()
cities.pop()
print(cities)

# pop(idx)
cities.pop(2)
print(cities)

# remove(val)
cities.remove("Banglore")
print(cities)


# sort() in Ascending
nums = [60,50,10,30,20,80,45]
nums.sort()
print(nums)

cities = ["Gwalior","Indore","Bhopal","Mumbai","Nasik","Pune","Chennai","Goa","Jabalpur"]
cities.sort()
print(cities)

# sort(reverse = True)  sort in descending
nums = [60,50,10,30,20,80,45]
cities = ["Gwalior","Indore","Bhopal","Mumbai","Nasik","Pune","Chennai","Goa","Jabalpur"]
nums.sort(reverse=True)
print(nums)
cities.sort(reverse=True)
print(cities)


# copy()
cities = ["Gwalior","Indore","Bhopal","Mumbai","Nasik","Pune","Chennai","Goa","Jabalpur"]
c = cities.copy()
print(c)

# len() find the length of object
print(len(cities))

# Clear()
c.clear()
print(c)

# del ,delete object
del c
print(c)

# count(val)
nums = [10,20,30,10,30,20,10,40,50]
print("The Count is",nums.count(20))

# index(val)
print(nums.index(50))


# list creation
l = []
lst = list()
print(lst)
# print(l)
lst.append(10)
lst.append(20)
lst.append(30)
lst.append(40)
print(lst)

for i in range(1,11):
    l.append(i)
print(l)


# concatenation
a = [1,2,3]
b = ['a','b','c']
c = a+b
print(c)
print(a+b)