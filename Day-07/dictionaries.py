# DICTIONARIES
# A dictionary is a built-in data type in python that stores data in key-value pairs.

# Creating and Accessing Dictionary Elements
student={
"name": "greeshma",
"age" : 22,
"branch":"ECE"
}
print(student)
print(student["name"])
print(student["age"])

# Adding and Updating Dictionary Elements
student["rollno"]= 20
print(student)

# Updating an existing key-value pair
student["age"]= 23
print(student)

# Removing Dictionary Elements
student.pop("branch")
print(student)
student.popitem() 
print(student)
student.clear()
print(student)

# Dictionary Methods
# keys() method returns a view object that displays a list of all the keys in the dictionary
dict1={
"name": "greeshma",
"age" : 22,
"branch":"ECE"
}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
