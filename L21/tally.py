def tally(vals):
    ''' counts occurrences in vals '''
    d={}
    for v in vals:
        v=v.lower()
        v = strip_punctuation(v)
        c = d.get(v,0)
        d[v]=c+1
    return d

def strip_punctuation(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while len(word)>0 and word[-1] not in alphabet:
        word = word[:-1]
    while len(word)>0 and word[0] not in alphabet:
        word = word[1:]
    return word

def test():
    with open('L21/RandJ.txt','r') as rfile:
        words = rfile.read().split()
    d = tally(words)
    wordcounts = sorted(d.items(),key=lambda x: x[1]*100-len(x[0]), reverse=True)
    return wordcounts

out = open('L21/RandJcounts.txt','w')
ws = test()
for i in range(len(ws)):
    line = f'{i} {ws[i]} \n'
    out.write(line)
out.close()
print('done')

