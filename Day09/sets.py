# Python Sets
# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

# Example:
info = {"Carla", 19, False, 5.9, 19}
print(info)
# Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set

# Accessing set items:
# Using a For loop
# You can access items of set using a for loop.

# Example:
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)


    Aman = {} # because set and dictionary have same sintex , so it will trat like a empty dict not empty set 
print(type(Aman))

#for creating an empty set 
Sohail = set()
print(type(Sohail))