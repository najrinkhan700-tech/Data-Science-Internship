"""
list -> list is the collection of elements that written in [].
orderd
indexd
Allow duplicates 
allow different type of data
Mutable or changeble

syntax -> list_name = [val1,val2,....,valn]

"""
data = ["Rahul",35,1031,89.7]
print(data)

# Mutability
data[0] = "Aman"
print(data)

# Indexing
print(data[3])
print(data[2])

cities = ["Gwalior","Indore","Bhopal","Mumbai","Nasik","Pune","Chennai","Goa","Jabalpur"]
print(cities[1])
print(cities[3])
print(cities[0])
print(cities[7])
print(cities[-1])
print(cities[-2])
print(cities[-9])

# Slicing
print(cities[1:5])
print(cities[4:7])
print(cities[-3:-6:-1])
print(cities[:7:2])
print(cities[::3])
print(cities[::])
print(cities[::-1])
print(cities[-1:-9:-2])


