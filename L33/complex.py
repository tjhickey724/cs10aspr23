class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def __str__(self):
        return f'{self.r} + {self.i}i'
    def __eq__(self,other):
        return self.r==other.r  and self.i==other.i


x = Complex(3.0, -4.5)
y = Complex(3.0,-4.5)
if x==y:
    print('x==y')
else:
    print('not equal')
print(x.r)
print(x.i)
print(x)