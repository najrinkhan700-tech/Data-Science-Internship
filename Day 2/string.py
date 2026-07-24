"""
String is the group or collection of alpha numeric characters that written in '', or "".
multilinne string - '''
"""
name = "Ravi"
print(name)

print("""hello
i am learning
python""")

print("A","B","C",sep="")
print("A","B","C",sep=" ")
print("A","B","C",sep="     ")
print("A","B","C",sep="*")
print("A","B","C",sep="\n")
print("A","B","C",sep="\t")
print("A","B","C",sep="/")
print("A","B","C",sep="11")   

# Indexing
# slicing
name = "Hello world"
print(name[1:7])   #range[start:stop-1:step]
print(name[1:3])
print(name[1:8:2])
print(name[::])
print(name[::-1])
print(name[-1:-10:-2])
print(name[-1:-11:-3])

line = "Hello i am learning python"
word = "python"
print(word in line)


# len() - return length
print(len(line))

# concatenation  +
print("A"+" "+"B")
name = "Ravi"
sname = "Singh"
print(name + " " + sname)
print("123"+"12")
print(123+12)


name = input("Enter name1 ::")
name2 = input("Enter name2::")
print(name + name2)


n1 = int(input("Enter a number::"))
n2 = int(input("Enter a number::"))
print(n1+n2)


