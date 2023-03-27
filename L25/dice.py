from random import randint

def dice(n):
    return [randint(1,7) for i in range(n)]

def coins(n):
    return [randint(0,1) for i in range(n)]

def dice2(n):
    num=[]
    for i in range(n):
        num.append(randint(1,7))
    return num

print(dice2(2))
#print(coins(10))