def top_half():
    for line in range(1, 5):
        print("|", end="")

        for space in range(0, line * -2 + 8):
            print(" ", end="")
        

        print("<>", end="")

        for dot in range(0, line * 4 - 2):
            print(".", end="")
        

        print("<>", end="")

        for space in range(1, line * -2 + 8):
            print(" ", end="")
        

        print("|")
top_half()