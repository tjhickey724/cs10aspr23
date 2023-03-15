'''
simple python programs to demo reading
and writing from files...
'''

def read_weather():
    " reads a file of temperatures and returns the list of floats"
    with open("L18/weather.txt") as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = float(data[i])
    return data

def read_weather_2():
    " reads a file of temperatures and returns the list of floats"
    with open("L18/weather.txt") as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = float(data[i])
    for i in range(1,len(data)):
        print(data[i-1]," to ",data[i],", change = ",data[i]-data[i-1])

def read_weather_3():
    with open("L18/weather.txt") as weather_file:
        data = weather_file.readlines()
        old = float(data[0])
    for i in range(len(data)):
        new= float(data[i])
        print(old, "to", new, ", change", (new-old))
        old=new

def temp_change(temps):
    for i in range(len(temps)-1):
        change = temps[i+1] - temps[i]
        print(temps[i+1],"to", temps[i],", change = ",change)
    


temp_change(read_weather())

#print(read_weather_3())
