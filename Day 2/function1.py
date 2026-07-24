def square(n):
    return n*n

x = square(9) #method1
print(x)

print(square(8)) #method2

def largest_num(a,b,c):
    if a > b and a > c:
        print("Larget:",a)
    elif b > a and b > c:
        print("Largest:",b)

    else:
        print("Largest:",c)

x = int(input("Enter value of x:")) 
y = int(input("Enter value of y:")) 
z = int(input("Enter value of z:")) 
largest_num(x,y,z)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)

x = int(input("Enter a number:"))
factorial(x)


def prime_num(n):
    for i in range(2,n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

prime_num(19)


def check_even_odd(n):
    if n % 2 == 0:
        print("Even",n)
    else:
        print("ODD",n)

check_even_odd(8)
check_even_odd(7)


def sum(a = 2, b = 0,c = 1):
    print(a + b + c)

# sum(1)
# sum(1,2)
# sum()
# sum(2,4,6) 


def sumOf_num(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)

sumOf_num(1,2,3)