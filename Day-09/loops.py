 # Loops in Python
# for loop
# A for loop is used to execute a block of code repeatedly for each item in a sequence.
for i in range(1,6):
    print(i)

# Iterating Through a List Using For Loop
lst=[10,20,30,40,50]
for num in lst:
    print(num,end = " ")

# Accessing List Elements Using Index
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])

# Separating Even and Odd Numbers into Two Lists
even_list=[]
odd_list=[]
for i in range(1,11):
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)

# Jumping Statements
# break statement
for i in range(10):
    if i==4:
        break
    print(i,end = " ")

# continue Statements
for i in range(10):
    if i==4:
        continue
    print(i,end = " ")

# Pass Statement
for i in range(10):
    if i==4:
        pass
    print(i,end = " ")

# Assert Statement
assert 10%2==0 # assert will be used in testing. 
print("error")

# While Loop
# Printing Numbers from 1 to 5 using while loop
i = 1
while i<=5:
    print(i ,end = " ")
    i+=1 
    print(i)
# Printing Numbers from 5 to 1 using while loop
i = 5
while i>=1:
    print(i ,end = " ")
    i-= 1
    print(i)

# Loop Termination using Break and Else
for i in range(10):
    if i==3:
        break
    print(i)
else:
    print("loop completed")

for i in range(10):
    if i==13:
        break
    print(i,end = " ")
else:
    print()
    print("loop completed")

# factors
num=int(input("enter a number:"))
for factor in range(1,num+1):
   if num% factor==0:
        print(factor)

# Counting odd numbers
num=int(input("enter a number:"))
count=0
for n in range(1,num+1):
    if n%2!=0:
        count= count+1
print("count of odd numbers:",count)

# prime number
num=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")

# perfect numbers
num=int (input("enter a number:"))
sum=0
for i in range(1,num):
    if num %i==0:
      sum+=i
if sum==num:
            print("perfect number")
else:
   print("not a perfect number")
# List opeartions using Loops
# minimum elements in a list
l=[10,26,2,4,45,-3]
mini=l[0] # float('inf')
for num in l:
    if num<mini:
        mini=num
    print(mini)
# maximum elements in a list
l=[10,26,2,4,45,-3]
maxi=l[0] # float('inf')
for num in l:
    if num>maxi:
        maxi=num
print(maxi)
# sum of elements in a list
lst=[1,2,3,4,5]
sum = 0
for num in lst:
    sum += num
    print(sum)
# Length of a list using a for loop
lst=[1,2,3,4,5]
length = 0
for num in lst:
    length +=1
    print(length)
