# Excersice 2:
# Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)



myTime = int(time.strftime('%H'))

if(myTime>=0 and myTime<12):
  print("Good Morning madam...")
elif(myTime>=12 and myTime<17):
 print("Good After noon sir...")  
elif(myTime>=17 and myTime<0):
 print("Good night sir...")   
    
    
