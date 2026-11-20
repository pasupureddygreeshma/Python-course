# Conditional Statements
# A conditional statements are the keywords to control the flow of execution.
# They are used to makeb the decision based on the condition on true or false.

# Types Of Conditional Statements
# if / simple if
# if else
# if elif
# Nested if

# if condition
age=int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote")

 # if else condition
age=int(input("enter your age:"))
if age>=18:
   print("you are eligible to vote")

else:
    print("you are not eligible to vote")

# if-elif-else condition
age=int(input("enter your age:"))
if age>=60:
    print("you are a senior citizen")
elif age>=18:
    print("you are a young adult")
else:
    print("you are a child")

#Nested if condition
age=int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote")
    if age>=60:
        print("you are a senior citizen")
    else:
        print("you are a young adult")
else:
    print("you are not eligible to vote")