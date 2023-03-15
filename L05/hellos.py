def print_hello_1():
    print('hello')
    print('hello')

def print_hello_2():
    print_hello_1()
    print_hello_1()

def print_hello_3():
    print_hello_2()
    print_hello_2()

def print_hello_4():
    print_hello_3()
    print_hello_3()

print_hello_4()