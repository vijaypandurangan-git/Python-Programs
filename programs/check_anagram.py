#Program to Check Anagrams
'''
What is an Anagram?
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
👉 Both words must contain the same letters, with the same frequency, but in a different order.

Examples of Anagrams:
listen → silent ✅
race → care ✅
night → thing ✅
hello → holle ✅
apple → papel ✅
earth → heart ✅
Not Anagrams:
hello → world ❌ (Different letters)
cat → actt ❌ (Extra 't' in second word) '''

def check_anagram(str1, str2):
    char_count1 = {}
    char_count2 = {}
    
    if len(str1) != len(str2):
        return False
    
    for char in str1:
        if char in char_count1:
            char_count1[char] = char_count1[char] + 1
        else:
            char_count1[char] = 1
        
    for char in str2:
        if char in char_count2:
            char_count2[char] = char_count2[char] + 1
        else:
            char_count2[char] = 1
            
    print("Character Frequency of First string:", char_count1)
    print("Character Frequency of Second String", char_count2)
    
    return char_count1 == char_count2                   
    
    return

str1 = input("Enter the first string:")
str2 = input("Enter the second string:")

if check_anagram(str1, str2):
    print("The words are Anagrams")
else:
    print("The words are not Anagrams")    