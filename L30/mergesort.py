import random
import time

def merge(vs,ws):
    i=0
    j=0
    vals=[0]*(len(vs)+len(ws))
    while (i<len(vs) and j<len(ws)):
        if vs[i]<ws[j]:
            vals[i+j]=vs[i]
            i=i+1
        else:
            vals[i+j]=ws[j]
            j=j+1
    # either i==len(vs) or j== len(ws)
    # one of the lists has been fully processed

    # copy rest of ws to list
    while j<len(ws):
        vals[i+j]=ws[j]
        j=j+1
    # copy rest of vs to list
    while i<len(vs):
        vals[i+j]= vs[i]
        i=i+1
    return vals

def mergesort(vals):
    n = len(vals)
    if n<=1:
        return vals
    mid = n//2
    vs = vals[:mid]
    ws = vals[mid:]
    vs = mergesort(vs)
    ws = mergesort(ws)
    vals = merge(vs,ws)
    return vals

def MStest(n):
    vals = [random.randint(0,10*n) for _ in range(n)]
    print('before sorting',vals)
    mergesort(vals)
    print('after sorting',vals)



def MStimetest(n):
    vals = [random.randint(0,10*n) for _ in range(n)]
    start = time.perf_counter_ns()
    mergesort(vals)
    end = time.perf_counter_ns()
    total = (end-start)/10**9 
    return total


if __name__=='__main__':
    MStest(4)
    n = int(input("n: "))
    print('time in seconds:',MStimetest(n))
        