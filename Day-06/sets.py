# SETS
# A set is a built-in data type in python that stores unordered and unindexed collection of unique elements.
# Creating a Set
set1={1,2,3,4,5}
print(set1)

# Set Methods
#Adding Elements to a Set
set1.add(6)
print(set1)

# Removing Elements From a Set
set1.remove(2)
print(set1)

# Discard Method
set1.discard(3)
print(set1)

# Copy Method
set1= {1,2,3,4,5}
set2=set1.copy()
print(set1)
print(set2)

# Clear Method
set1.clear()
print(set1)

# Set Operations
# Union Of Two Sets
s1={10,20,30,40}
s2={40,50,60}
print(s1.union(s2))

# Intersection Of Two Sets
print(s1.intersection(s2))

# Difference Of Two Sets
print(s1.difference(s2))
print(s2.difference(s1))

# Symmetric Difference Of Two Sets
print(s1.symmetric_difference(s2))

# Subset and superset
s3={26,45,18,1,4}
s4={26}
print(s3.issuperset(s4))
print(s4.issubset(s3))
