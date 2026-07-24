# for i,v  in range(start,stop-1,step):
#     code

for i in range(1,100):
    if i % 3 == 0:
        print(i)


import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) 


import math

x = math.pi

print(x)

# nested loop

for i in range(1,6):       # 1
    for j in range(1,6):   #1,2,3,4,5
        print(j,end="")  

    print()


import time
print("Heloo")
time.sleep(6)
print("I am learning python")
count = 0
for i in range(1,21):
    time.sleep(1)
    print(i)
    count = count+1
print("Total seconds",count)




for i in range(1,11):
    print(i**2)


n = int(input("Enter a number::"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)

for i in range(1,11):
    # print(n*i)
    print(n,"X",i,"=",n*i)

# prime number  10,3,5,11
n = int(input("Enter a number::"))
for i in range(2,n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime number")

# Nested loop
for i in range(1,6): 
    for j in range(1,i+1):
        print("*",end = "")
    print()

n = int(input("Enter a number::"))
for i in range(10,0,-1):
    print(n,"X",i,"=",n*i)
    

