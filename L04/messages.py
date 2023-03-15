def message1():
    print("This is message1.")


def message2():
    print("This is message2.")
    message1()
    print("Done with message2.")

message1()
message2()
print("Done with everything.")
