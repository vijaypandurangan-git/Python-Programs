#count frequency of characters in a string

def count_each_character_frequency(sentence):
    character_frequency = {}
    
    for char in sentence:
        if char != " " :
            if char in character_frequency:
                character_frequency[char] = character_frequency[char] + 1
            else:
                character_frequency[char] =1
            
    #print("Character Frequency is:", character_frequency)   
    for char,count in character_frequency.items():
        print(f"{char} : {count}") 
 
sentence = " johnny johnny yes papa eating sugar no papa"    


count_each_character_frequency(sentence)