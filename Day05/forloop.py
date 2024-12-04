# Introduction to Loops
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

# for loop
# while loop
# The for Loop
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# Example: iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")


# Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

# Similarly, we can use loops for lists, sets and dictionaries.

# range():
# What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

# Here, we can use the range() function.
for k in range(5):
    print(k)

# Here, we can see that the loop starts from 0 by default and increments at each iteration.

# But we can also loop over a specific range.
for k in range(4,9):
    print(k)

for i in (0,10,2):#print only given value ,its itrate all the element given
    print(i)
for i in range(0,10,2): #Range function will itrate somthing like , start from 0 and with 10 and always print 2 steps,(i+2)
    print(i)   


