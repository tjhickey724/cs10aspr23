from random import choice;

with open('words.txt','r') as wfile:
    words = wfile.read().split()

words = [w for w in words if len(w)==5]

for i in range(10):
    w = choice(words)
    print(w)


