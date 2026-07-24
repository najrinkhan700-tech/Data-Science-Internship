i = 2
while(i<=10):
    print(i)
    i = i + 2

# check pallindrome string
name = input("Enter string::")
rev = name[::-1]

if rev == name:
    print("Pallindrome")
else:
    print("Not pallindrome")

# pallindrome number
digit = int(input("enter a digit::"))
n = digit
sum = 0
while(n>0):
    r = n % 10
    sum = sum * 10 + r
    n = n // 10
print("Reverse",sum)
if sum == digit:
    print("Pallindrome")
else:
    print("Not pallindrome")

# # break statement
for i in range(1,10):
    if i == 4:
        break
    print(i)


# # continue statement
for i in range(1,10):
    if i == 4:
        continue
    print(i)


# Armstrong number
# 153 
# 1 , 125, 27 
# 153

digit = int(input("Enter a number::"))
n = digit
sum = 0
while(n>0):
    r = n % 10
    sum = sum + r ** 3
    n = n // 10
if sum == digit:
    print("Armstrong number",sum)
else:
    print("Not Armstrong",sum)

# swapping of two number
a = 5
b = 10

# a,b = b,a
temp = a
a = b
b = temp
print(a,b)

