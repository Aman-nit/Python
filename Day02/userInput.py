# Taking User Input in python
# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable
variable=input()

# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

variable=int(input())
variable=float(input())

# We can also display a text using input function. This will make input() function take user input and display a message as well

a=input("Enter the name: ")
print(a)

a = input("Enter your name: ")
print("My name is", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x  + y)

print(int(x) + int(y))