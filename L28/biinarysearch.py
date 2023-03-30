import random
def binarysearch(val,vals):
    return binarysearchRecursive(val,vals,0,len(vals)-1)

def binarysearchRecursive(val,vals,lo,hi):
    if lo>hi:
        return -1
    else: 
        mid = (lo+hi)//2
        print(f'lo={lo} mid={mid} hi={hi} val={val} vals[{mid}]={vals[mid]}')
        if vals[mid]==val:
            return mid
        elif val < vals[mid]:
            return binarysearchRecursive(val,vals,lo,mid-1)
        else:
            return binarysearchRecursive(val,vals,mid+1,hi)
    
def randlist(n):
    mean = random.randint(20,80)
    return [int(round(random.gauss(mean,40))) for i in range(n)]

def test():
    vals = randlist(100)
    val = vals[0]
    vals = sorted(vals)
    print('search for',val)
    print('in the list', vals)
    print('-'*50)
    result = binarysearch(val,vals)
    print('result is',result)

    val = val+1
    print('now search for',val)
    result = binarysearch(val,vals)
    print('result is',result)


test()