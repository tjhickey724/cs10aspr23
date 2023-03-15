with open('courses.csv','r') as coursefile:
    courses = coursefile.readlines()

for course in courses[:3]:
    print(course)
    fields = course.split(',')
    print(fields)
    print('-'*30)

for course in courses:
    fields = course.split(',')
    enr = int(fields[-1])
    if enr>200:
        print(course)
