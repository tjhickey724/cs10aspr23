import random
begin=input("Would you like to play?")
while begin=="yes": 
    target=random.randint(0,100)
    guess=int(input("take a guess"))
    while guess!= target: 
        if guess>target:
            print("Too high")
            guess=int(input("take a guess"))
        if guess<target:
            print("Too low")
            guess=int(input("take a guess"))
    print("You win")
    print("Would you like to play?")
print("Bye")