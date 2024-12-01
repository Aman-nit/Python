#                       All varriables are in object form in Python

# What is a variable?
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

a = 1
b = True
c = "Harry"
d = None

# What is a Data Type?
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

a = 1
print(type(a))
b = "1"
print(type(b))

# 1. Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i

# 2. Text data: str
# str: "Hello World!!!", "Python Programming"

# 3. Boolean data:
# Boolean data consists of values True or False.

# 4. Sequenced data: list, tuple
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list5 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list5)

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tupleAman = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tupleAman)

# 5. Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)