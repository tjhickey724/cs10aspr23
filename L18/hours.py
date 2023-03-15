def calculate_hours():
    with open('L18/hours.txt','r') as file:
        data = file.readlines()
    for line in data:
        vals = line.split()
        total_hours=0
        for i in range(2,len(vals)):
            vals[i] = float(vals[i])
            total_hours += vals[i]
        avg_hour = total_hours/(len(vals)-2)
        print(vals[1],"ID#"+vals[0],'worked',round(total_hours,1),\
              'hours (',round(avg_hour,1),' hours/day)/day')
        #print(vals)

    #print(data)

calculate_hours()
