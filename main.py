# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

# are anagrams of each other 

N_O_C = 256

  
# Function to check if two strings 
# are anagrams of each other 

def find_anagram(word1, word2): 

      

    # Creating a count array and initialize 

    count=[0 for i in range(N_O_C)] 

    i=0
    # count array 

    for i in range(len(word1)): 

        count[ord(word1[i]) - ord('a')] += 1; 

        count[ord(word2[i]) - ord('a')] -= 1; 


    if(len(word1) != len(word2)): 

        return False; 



    for i in range(N_O_C): 

        if (count[i] != 0): 

            return False        

      

    return True

  
# User input

word1=input("Enter 1st word : ")

word2=input("Enter 2nd word : ")

  
#  call function

if (find_anagram(word1, word2)): 

    print( True,

    "The two words are anagram of each other") 

else: 

    print( False,

    "The two words are not anagram of each other") 

    

 

