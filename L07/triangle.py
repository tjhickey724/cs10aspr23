SIZE=20
def draw_triangle():
    '''
        draws this figure with 20 lines
        *
        **
        ***
        ****
        *****
        ....
        ****....**** 
    '''
    for i in range(1,SIZE+1):
        print('*'*i)

SIZE2=4
def draw_triangle2():
    '''
       draws a triangle
       leaning to the right
           *
          **
         ***
        ****
        ...
        of height 9...
    i  spaces pluses(i)
    1  8      1
    2  7      2
    3  6      3
    4  5      4 
    '''
    for i in range(1,SIZE2+1):
        print(" "*(SIZE2-i), end="")
        print("+"*i)

draw_triangle2()

SIZE3=9
def draw_triangle3():
    for line in range(1, SIZE3):
        for space in range(1, SIZE3-line):
            print(" ",end="" )       
        for dot in range(1,line ):
            print("+",end="")
        print()
draw_triangle3()