# if condition -> 
# 100 - >50
#  syntax   
# if condition:
#     expression

# Check eligibility    
age = int(input("Enter age::"))
if age >= 18:
    print('U can vote')
else:
    print("U can not vote")

num = int(input("Enter a number::"))
if num % 2 == 0:
    print("Even")
else:
    print("ODD")

actual_pass = "Najrin@133"
password = input("Enter password::")

if password == actual_pass:
    print("This is Dashboard")
else:
    print("Please enter right password..")

price = int(input("Enter price::"))
if price >= 5000:
    print(price - (price*0.25))
elif price >= 4000:
    print(price - (price*0.2))
elif price >= 2000:
    print(price-(price*0.1))
else:
    print(price)

num = int(input('Enter number::'))
if num % 5 == 0 and num % 3 == 0:
    print("Yes Divisible by both numbers 3,5")
else:
    print("Not divisible..")


a = int(input('Enter a number'))
b = int(input('Enter a number'))
c = int(input('Enter a number'))

if a > b and a > c:
    print(a," is greater")

elif b > a and b > c:
    print(b,"is greater")

elif c > a and c > b:
    print(c,"is greater")
else:
    print("Drop")

char = input("Enter a charecter::")
if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
    print("Vowel")
else:
    print("Consonant")


# .isalpha()
# .isdigit()
char = input("Enter a charecter::")
if char.isalpha():
    print(char,"is alphabet")
elif char.isdigit():
    print(char,"is a digit")
else:
    print("special charecter")



n = int(input("Enter a number::"))

for i in range(1,11):
    # print(i*num)
    print(n ,"X",i,"=",n*i)

4 = 4*3*2*1
5 = 5*4*3*2*1
fact = 1
for i in range(1,n+1):
    fact = fact * i    # 1 2 6 24 120
print(fact)

sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)

