#python compile by interpreter
# Python Comments
# A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

# Single-Line Comments:
# To write a comment just add a ‘#’ at the start of the line.

#This is a 'Single-Line Comment'
print("This is a print statement.")
print("Hello World !!!") #Printing Hello World

# Multi-Line Comments:
# To write multi-line comments you can use ‘#’ at each line or you can use the multiline string

#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")


#     Escape Sequence Characters
# To insert characters that cannot be directly used in a string, we use an escape sequence character.

# An escape sequence character is a backslash \ followed by the character you want to insert.

# An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

# print("This doesnt "execute")
print("This will \" execute")

# More on Print statement
# The syntax of a print statement looks something like this:

#print(object(s), sep=separator, end=end, file=file, flush=flush)

# Other Parameters of Print Statement
#1. object(s): Any object, and as many as you like. Will be converted to string before printed
#2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
#3. end='end': Specify what to print at the end. Default is '\n' (line feed)
#4. file: An object with a write method. Default is sys.stdout
#5. Parameters 2 to 4 are optional

print("Hello Aman", 7 , 8, sep="__",end=".")
# here we change the bydefault new line corrector with (.)
print("How are you")

