# Finally Clause
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# Syntax:
# try:
#    #statements which could generate 
#    #exception
# except:
#    #solution of generated exception
# finally:
#     #block of code which is going to 
#     #execute in any situation
# The finally block is executed irrespective of the outcome of try……except…..else blocks
# One of the important use cases of finally block is in a function which returns a value.

# Example:
#in this case if we remove word finally and use normal print or any function call both will work same 
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")


# Example.02:
#in this case if we remove word finally and use normal print or any function then it will not run because function already returned some value 
#But if we use finally in function even after function returned any value it will always run 
print("Example 02")
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)