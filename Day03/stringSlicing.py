# String Slicing & Operations on String
# Length of a String
# We can find the length of a string using len() function.

# Example:
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# String as an array
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

# Example:
pie = "ApplePie"
print(pie[:5]) #its print element from 0 index to till 5th char
print(pie[6])	#returns character at specified index
# Note: This method of specifying the start and end index to specify a part of a string is called slicing.


pie = "ApplePie"
print(pie[:5])      #Slicing from Start[0 : 5]
print(pie[5:])      #Slicing till End [5 : len(pie)]
print(pie[2:6])     #Slicing in between(2nd index to 6-1 index)
print(pie[-8:])     #Slicing using negative index [len(pie) - 8 : len(pie)]
print(pie[-4:-2])   #Slicing using negative index [len(pie) - 8 : len(pie)-2]

# Loop through a String:
# Strings are arrays and arrays are iterable. Thus we can loop through strings.

# Example:
alphabets = "ABCDE"
for i in alphabets:
    print(i)

    print(pie[2:6]) 