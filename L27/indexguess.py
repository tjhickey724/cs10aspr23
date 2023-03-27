'''
indexguess.py is a game to guess the index of a list
which contains a particular number.
'''
from random import randint, choice 

def play_many():
    response = input("Do you want to play? (y or n) ")
    while response=='y':
        n = int(input("what size list? "))
        play_game(n)
        response=input("Want to play again? (y or n) ")
    print('goodbye')

 
def play_game(n):
    ''' play a game with a list of size n'''   
    # generate a list of n random numbers
    vals = create_list(n)
    # then we pick a random index in the list
    index = randint(0,n-1)  
    # then we ask the user to try to guess it
    # and we count their attempts
    game_loop(vals,index)

def create_list(n):
    ''' generate a list of n random
        number in the range from lowest to highest
        which we don't tell the user...
    '''
    lowest = randint(0,n//2)
    highest = randint(10*n,100*n)
    vals = [randint(lowest,highest) for i in range(n)]
    vals.sort()
    return vals


def game_loop(vals,index):
    ''' ask the user to guess the index and give hints '''
    num = vals[index]
    print('try to guess the index of the list of length',len(vals),end=" ")
    print('which contains the value',num)
    counter=0
    guess=-1
    
    while guess!=index:
        print('guess the index of',num,end=" ")
        guess = int(input(": "))
        counter = counter+1
        print('vals[',guess,']=',vals[guess])

    print('you guessed it in',counter,'guesses')


play_many()