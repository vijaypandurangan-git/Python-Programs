sentence = "Johnny johnny yes yes yes Papa eating sugar no papa"
words = sentence.lower().split()

words_frequency = {}

for word in words :
    if word in words_frequency:
        words_frequency[word] = words_frequency[word] + 1
    else:
        words_frequency[word] = 1

print( "Words frequency dictionary", words_frequency )
print('Duplicated words:')

for word,count in words_frequency.items() :
    if count>1:
        print(f"{word} {count} Times")            