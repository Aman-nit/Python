def factorial(n):
    if(n ==0 or n ==1):
        return n
    else:
        return n*factorial(n-1)
    
print(factorial(5))   



def fabonaci(n):
    if(n ==0 or n ==1):
        return n
    else:
        ans =fabonaci(n-2)+fabonaci(n-1)
        print(f"{ans}  ") 
        return ans

n = int(input("Enter a number :-"))
fabonaci(n)