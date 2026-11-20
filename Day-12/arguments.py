# Types of Arguments
# 1. Positional Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("Greeshma", 22)

# 2. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=22, name="Greeshma")

# 3. Default Arguments
def student(name, age=22):
    print("Name:", name)
    print("Age:", age)
student("Greeshma")

# 4. Variable-Length Arguments (*args)
def add(*args):
    total = 0
    for i in args:
        total = total + i
    return total
result = add(10, 20, 30, 40)
print(result)

# 5. Variable-Length Keyword Arguments (**kwargs)
def student(**kwargs):
    print(kwargs)
student(name="Greeshma", age=22, course="Python")
# Scope in Python

# 1. Local Scope
def student():
    name = "Greeshma"
    print(name)

student()
# 2. Enclosed Scope
def outer():
    x = 10
    def inner():
        print(x)
    inner()
outer()

# 3. Global Scope
x = 10
def display():
    print(x)
display()
print(x)

# 4. Built-in Scope
numbers = [10, 20, 30]
print(len(numbers))
print(sum(numbers))
print(max(numbers))

# Global and Nonlocal Keywords
# 1. Global Keyword
x = 10
def change():
    global x
    x = x + 1
change()
print(x)

 # 2. Nonlocal Keyword
def outer():
    x = 10
    def inner():
        nonlocal x
        x = x + 5
        inner()
    print(x)
outer()

# Pass by Object Reference
def display(x):
    print(x)
    x = x + 10
    print(x)
a = 100
display(a)
print(a)

# Recursion
# Factorial Using Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# Sum of Natural Numbers Using Recursion
def natural_sum(n):
    if n == 1:
        return 1
    return n + natural_sum(n - 1)
print(natural_sum(5))