'''
Python scripts to solve crossword problems...
'''

with open('words.txt','r') as wordfile:
    words = wordfile.readlines()
# clean the list by stripping white space off of each word
for i in range(len(words)):
    words[i]=words[i].strip()


def q3t():
    # find all words of length 5
    # starting with q and ending with t
    for word in words:
        if word[0]=='q' and len(word)==5 and word[4]=='t':
            print(word)

def mla1():
    for word in words:
        if len(word)==6 and word[1]=='e' and word[3]=='u' and word[5]=='y':
            print(word)

def findVowel():
    list='aeiou'
    for word in words:
        if len(word)==5 and word[1] in list and word[2] in list and word[3] in list:
            print(word)
findVowel()