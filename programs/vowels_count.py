#Count vowels in a string

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in sentence:
        if char in vowels:
            count = count + 1
    return count

some_string = str(input('Enter the string:'))
print("Vowel count is ",count_vowels(some_string) )     
    