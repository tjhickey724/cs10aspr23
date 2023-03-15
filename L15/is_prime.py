def is_prime(n):
    ''' returns true if n is prime, false otherwise 
        a number n is prime if the only numbers between 1 and n
        that divide it evenly are 1 and n.
        This is a buggy program!
    '''
    for d in range(2,n):
        if n%d==0:
            return False
    return True

for i in range(2,20):
    if is_prime(i):
        print(i,'is prime')
    else:
        print(i,'is not prime')

