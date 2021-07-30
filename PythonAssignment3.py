#Assignment 3
#whether check string is pangram
		
import string 
alphabet = string.ascii_lowercase
  
def ispangram(sentence):
    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True
sentence = input('enter a sentence')
if(ispangram(sentence) == True):
    print("Given String is Pangram")
else:
    print('Given String is Not Pangram')