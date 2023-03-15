def div2(a,b):
    return (a//b, a%b)

(u,v) = div2(100,7)
print(u,v,u*7,u*7+v)

def test(a,b,c,d):
    return [[a,b],[c,d]]

[[x,y],[z,w]] = test(1,2,3,4)
print(x,y,z,w)
