'''
create a table of numbers from 1 to n
and their squares and squareroots
and store it in a file squares.csv
'''
import math

def main():
    n = int(input("enter n: "))
    outfile = open('L20/squares.csv','w')
    outfile.write("n,n*n,sqrt(n)\n") # column names in excel100

    for i in range(n+1):
        line = str(i)+','+str(i*i)+','+str(math.sqrt(i))
        outfile.write(line+"\n")
    outfile.close()

main()