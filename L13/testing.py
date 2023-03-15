def rotate(letter):
    num = ord(letter)
    new_num = num +3
    if new_num>122:
        new_num = new_num-26
    new_letter = chr(new_num)
    return new_letter

def translate(word):
    for w in word:
        if w==' ':
            print(' ',end='')
        else:
            print(rotate(w),end="")

translate('attack at dawn')
