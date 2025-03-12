def count_word_occurences(sentence):
    #words= sentence.lower().split() # if we want to consider lower and upper case as same, convert all to lowercase
    words = sentence.split() # this will treat lower and upper case as separate word
    word_frequency = {}
    
    for word in words:
        if word in word_frequency:
            word_frequency[word]= word_frequency[word] + 1
        else:
            word_frequency[word] = 1
    print("Word Frequency Dictionary is:", word_frequency )                        

sentence = "Hey this is, the hey, this why aint you. author hey myself is this why"  

count_word_occurences(sentence)  