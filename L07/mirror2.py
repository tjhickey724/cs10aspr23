SIZE = 10;

# Prints the expanding pattern of <> for the top half of the figure.
def top_half(): 
    for line in range(1, SIZE):
        print("|", end="")

        for space in range(1, line * -2 + (2*SIZE) + 1):
            print(" ", end="")
        

        print("<>", end="")

        for dot in range(1, line * 4 - 3):
            print(".", end="")
        

        print("<>", end="")

        for space in range(1, line * -2 + (2*SIZE) + 1):
            print(" ", end="")
        

        print("|")
top_half()