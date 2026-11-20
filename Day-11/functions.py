# Creating a Function
def greet():
    print("Hello")
greet()

# Function With Parameters
def add(a, b):
    print(a + b)
add(10, 20)

# Return Statement
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# Four Types of Functions
# 1. Without Parameters and Without Return Value
def add():
    a = 10
    b = 20
    print(a + b)
add()

# 2. With Parameters and Without Return Value
def add(a, b):
    print(a + b)
add(10, 20)

# 3. Without Parameters and With Return Value
def add():
    a = 10
    b = 20
    return a + b
result = add()
print(result)

# 4. With Parameters and With Return Value
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
