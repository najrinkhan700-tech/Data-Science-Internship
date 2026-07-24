a = {10,20,30,40,50,60,10,10,20,30}
print(a)
print(type(a))
print(len(a))

# add element in set
# add()
# update()

fruits = {"Apple","Banana","Cherry"}
print(fruits)
fruits.add("Kiwi")
print(fruits)  # using add method


lst = ("Mango", "Orange")
fruits.update(lst)  # using update method
print(fruits)


# remove element
# remove()
# discard()
print(fruits)
fruits.remove("Cherry")
print(fruits)

fruits.discard("Banana")
print(fruits)

x = fruits.pop()  # its remove any element by default
print(x)
print(fruits)

fruits.clear()
print(fruits)

del fruits
print(fruits)

# join sets
# union() , |
# intersection(), &
# difference(), -
# symmetric difference , ^

set1 = {1,2,3,4}
set2 = {1,2,5,6}
set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

set3 = set1.intersection(set2)
set3 = set1 & set2
print(set3)


# difference method   
set3 = set1.difference(set2)  # it returns data that are not present in set 2
print(set3)

set3 = set1.symmetric_difference(set2)   # it returns unique values from both sets
print(set3)

# copy set
set4 = set1.copy()
print(set4)


# create a set
fruits = set()
print(type(fruits))
lst = ["Mango", "Orange","Kiwi", "Apple","Cherry"]
fruits.update(lst)  # using update method
print(fruits)
