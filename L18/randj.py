'''
Reads Romeo and Juliet and answer some questions ...
'''

def read_randj():
    with open("L18/RandJ.txt","r") as file:
        lines = file.readlines()
    return lines

text =read_randj()
for i in range(10):
    print(text[i])

def find_love():
    ''' prints all lines of RandJ containing word love'''
    text = read_randj()
    for line in text:
        if "love" in line:
            print(line)

find_love()


