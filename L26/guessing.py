import random

def play_game():

    play_again="yes"
    while play_again=="yes":
        #generate a random number from 1 to 100
        g = random.randint(1, 100)
        
        while True:
            #ask the user for a number n
            n = int(input("Guess a number between 1 and 100: "))
            
            #compare the user's number with your number
            #generate a response: too high, too low, or you win
            if n > g:
                print("Too high!")
            elif n < g:
                print("Too low!")
            else:
                print("You win!")
            #go back to 2 if the user didn't win
                break
            
        #ask if they want to play again
        play_again = input("Do you want to play again? (yes/no)")
        

play_game()