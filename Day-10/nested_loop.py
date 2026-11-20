# Square Star Pattern Using Nested For Loops
for r in range(4):
    for c in range(4):
        print("*", end=" ")
    print()

# Rectangle Star Pattern Using User Input
rows = int(input("enter no. of rows:"))
columns = int(input("enter no. of columns:"))
for r in range(rows):
    for c in range(columns):
        print("*",end = " ")
    print()

# Hallow Squares
for i in range(4):
    for j in range (4):
        if i==0 or i==3 or j==0 or j==3:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()

# Diagonal X Pattern
n=5
for i in range(5):
    for j in range(5):
        if i==j or (i+j)==(n-1):
            print("*",end=" " )
        else:
            print(" ", end =" ")
    print()
# Row-Wise Number Pattern
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
# Column-Wise Number Pattern           
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

# repeated Number Patterns
n=4
for i in range(n):
    print("*" *n)

# even and odd Number Patterns
even=2
odd=1
for i in range(4):
    for j in range(4):
       if i % 2==0:
        print(odd,end=" ")
        odd+=2
       else: 
        print(even,end=" ")
        even+=2
    print()

for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n=1
for i in range(1,5):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()

for i in range(1,5):
    for j in range(i):
        print(j,end=" ")
    print()

for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()

n=4
for i in range(4):
    for j in range(n-i):
        print("*",end=" ")
    print()

for i in range(1,5):
    for j in range(1,5):
        if i+j==n-1:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=3
for i in range(n):
    #spaces
    for j in range(n-i-1):
        print(" ",end=" ")
    #stars
    for j in range(2*i+1):
        print("*",end=" ")
    print()
            
n=5
for i in range(n):
    #spaces
    for j in range(n-i-1):
        print(" ",end=" ")
    #stars
    for j in range(2*i+1):
        print("*",end=" ")
    print()
n=4
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(2*n-(2*i+1)):
        print("*",end=" " )
    print()
