def read_data():
    infile = open("L20/courses.csv","r",encoding="utf-8")
    data = list(csv.reader(infile))
    return data
