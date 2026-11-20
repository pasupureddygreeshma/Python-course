 #Python Strings

# 1. Creating Strings
name = "Greeshma"
city = "Hyderabad"
message = "This is a multi-line string"

print("Name:", name)
print("City:", city)
print("Message:", message)


# 2. Accessing Characters (Indexing)
x = "Python"

print(x[0])
print(x[1])
print(x[-1])


# 3. String Slicing
text = "Python"

print(text[0:3])
print(text[2:])
print(text[:3])
print(text[::-1])


# 4. String Concatenation
str1 = "Hello"
str2 = "Python"

str3 = str1 + " " + str2
print(str3)


# 5. String Repetition
s1 = "Python"
print(s1 * 4)


# 6. String Methods
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.replace("python", "Java"))


# 7. String Checking Methods
str1 = "Codegnan Institute @123"

print(str1.islower())
print(str1.isupper())
print(str1.isalpha())
print(str1.isalnum())
print(str1.isdigit())
print(str1.isspace())


# 8. String Whitespace Methods
x = "  Hello Greeshma  "

print(x.strip())
print(x.lstrip())
print(x.rstrip())
print(x.replace(" ", ""))


# 9. Split and Join
name = "my name is Jancani"

print(name.split())

words = ["my", "name", "is", "Jancani"]
print(" ".join(words))


# 10. Built-in Functions
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

text = "Python Programming"
print(text.count("P"))