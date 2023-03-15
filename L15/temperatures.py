def main():
    days = int(input("How many days: "))
    temps = [0]*days
    for i in range(days):
        temps[i] = float(input("Day "+str(i+1)+"'s high temp: "))
    sum = 0
    for temp in temps:
        sum  = sum + temp
    avg = sum/len(temps)
    count=0
    for temp in temps:
        if temp>= avg:
            count = count+1
    print("the average temperature was",round(avg))
    print("there were",count,"days with above average temperature")

main()

