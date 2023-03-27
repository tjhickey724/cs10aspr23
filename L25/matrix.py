matrix = [[0,1,2,3], [4,5,6,7], [8,9,10,11]]

flattened = [i for row in matrix 
                 for i in row]

print('a',flattened)

flatten=[]
for row in matrix:
    for i in row:
        flatten.append(i)
print('b', flatten)