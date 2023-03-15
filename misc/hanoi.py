'''
iterative solution to towers of hanoi
the algorithm is pretty easy to write
but I don't know a simple proof
'''
def hanoi(n):
    s1=list(range(1,n+1))+[1000]
    s2=[1000]
    s3=[1000]
    h=[s1,s2,s3]
    print('start',h)
    while True:
        legal_move(0,1,h)
        if done(h,1,n): return
        legal_move(0,2,h)
        legal_move(1,2,h)
        if done(h,2,n): return
        legal_move(0,1,h)
        legal_move(2,0,h)
        if done(h,0,n): return
        legal_move(1,2,h)

def done(h,i,n):
    return len(h[i])==n+1

def move(i,j,h):
    top=h[i][0]
    h[j]=[top]+h[j]
    h[i]=h[i][1:]
    print(f'move {top} from {i} to {j}',h)


def legal_move(i,j,h):
    if h[i][0]<h[j][0]:
        if len(h[i])>1:
            move(i,j,h)
    else:
        if len(h[j])>1:
            move(j,i,h)

n = int(input("enter n: "))
hanoi(n)
