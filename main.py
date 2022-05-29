# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(w1, w2):
    # [assignment] Add your code here
    return sorted(w1) == sorted(w2)

w1 = input("Enter first word : ")
w2 = input("Enter second word : ")
print (find_anagrams(w1, w2))

