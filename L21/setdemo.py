rjfile = open('L21/RandJ.txt','r')
words = rjfile.read().split()
rjfile.close()
print(len(words),'words in RandJ')
unique_words_set = set(words)
print('the number of unique words is',len(unique_words_set))
unique_words_list = sorted(unique_words_set)
print(unique_words_list[:100])

