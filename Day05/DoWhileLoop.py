# Do-While loop in python
# do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# How to emulate do while loop in python?
# To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

# The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

# Example
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
#if not number > 0 evaluates to True if the  number is not positive If the user enters a non-positive number (like 0 or a negative number), the loop ends with the break statement



i= 0
while True:
    print(i)
    i = i+1
    if(i>5):
        break