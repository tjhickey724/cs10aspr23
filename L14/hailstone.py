def hailstone(n):
   ''' returns n//2 if n is even and 3n+1 if n is odd.''' 
   if n%2 == 0:
      return n//2
   else: 
      return 3*n+1

def main():
    ''' ask for an int and find the hailstone '''
    x = int(input("Enter a number: "))
    while x != 1:
        x = hailstone(x)
        print(x,end=" ")
    print('done')

main()