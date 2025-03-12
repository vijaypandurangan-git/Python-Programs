def check_anagram(str1, str2):
    char_count1 = {}
    char_count2 = {}
    
    if len(str1) != len(str2):
        return False
    
    for char in str1:
        if char in char_count1 :
            char_count1[char] +=1
        else:
            char_count1[char] = 1
            
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    
    print("Character frequency of 1st string", char_count1)
    print("Character frequency of 2nd string", char_count2)
    
    return char_count1 == char_count2                

str1 = input("Enter 1st string:")
str2= input("ENter 2nd string:")

if check_anagram(str1, str2):
    print("The words ARE ANAGRAMS")
else:
    print("The words are NOT ANAGRAMS")