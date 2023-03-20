'''
babynames.py
In this file we read the 1000 most popular baby names
into a list of dictionaries and then we plot the data
using matplotlib
'''

import csv
import matplotlib.pyplot as plt


# first we read the data into a list of names
file = open('names2000.csv','r')
reader = csv.DictReader(file)
names=[]
for row in reader:
    names.append(row)
print('number of names:',len(names))


# next we prepare it for analysis
# by making the count and year fields integers rather than strings
for name in names:
    name['count'] = int(name['count'])
    name['year'] = int(name['year'])


# here we sort the names by the most popular
popnames = sorted(names,key = lambda x: x['count'], reverse=True)

# here is a function to lookup the popularity of a name in a year
def popularity(name,gender,year):
    d = [x['count'] for x in names if x['name']==name and x['gender']==gender and x['year']==year]
    if d==[]:
        return 0
    else:
        return d[0]


# now we define a function to plot the popularity of a name
def plotName(name, gender):
    target = [x for x in names if x['name']==name and x['gender']==gender]
    years = [x['year'] for x in target]
    count = [x['count'] for x in target]
    plt.plot(years,count,label=name+":"+gender)


# here is a function to plot the popularity of several names
def plotNames(names,gender):
    for name in names:
        plotName(name,gender)
    plt.grid()
    plt.legend()

plotNames(['Timothy','Ryan'],'M')


