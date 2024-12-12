# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode


import random
import string

def rando_srtring3(length):
  return ''.join(random.choices("string.ascii_lowercase", k =length))
 



st = input("Enter a message: ")
words = st.split(" ")
coding = input("1 for Coding 0 for Decodig: ")
coding = True if (coding == "1") else False
if(coding):
  encoded_wordds =[]
  for word in words:
    if(len(word) >= 3):
      stnew = rando_srtring3(3) + word[1:] +word[0] + rando_srtring3(3)
      encoded_wordds.append(stnew)
    else:
      encoded_wordds.append(word[::-1])
    finalSt = " ".join(encoded_wordds)
  print("Encoded message: ",finalSt) 

else: 
    decoded_words = []
    for word in words:
        if len(word) >= 3:  # At least 6 chars (2 random + original word >= 3 + 2 random)
            original_word = word[3:-3]  # Remove random strings
            decoded_word = original_word[-1] + original_word[:-1]  # Rearrange to original
            decoded_words.append(decoded_word)
        else:
            word = word[::-1]
            decoded_words.append(word)
    stn = " ".join(decoded_words)
    print("Decoded message: ", stn)