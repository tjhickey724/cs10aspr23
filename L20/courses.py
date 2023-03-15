'''
This file is for analyzing Brandeis courses
'''
import csv

def read_data():
    infile = open("L20/courses.csv","r",encoding="utf-8")
    data = list(csv.reader(infile))
    return data

courses = read_data()
# for i in range(10):
#     print(courses[i])

# print courses with over 250 students
for course in courses:
    if int(course[-1])>250:
        print(course)

# counts courses over 100
def course_count(n):
    count = 0
    for course in courses:
        if int(course[-1])>n:
            count+=1
    return count

def subject_counts(subj):
    count=0
    total_enrollments=0
    for course in courses:
        if course[0]==subj:
            count += 1
            total_enrollments += int(course[-1])
    print(subj,'had',count,'courses, enrolling',total_enrollments,\
          'average class size was',total_enrollments/count)




def inst_counts(inst):
    count=0
    total_enrollments=0
    for course in courses:
        if inst in course[6]:
            count += 1
            total_enrollments += int(course[-1])
    print(inst,'taught',count,'courses, enrolling',total_enrollments,\
          '\nThe average class size was',total_enrollments/count)

def subject_year_counts(subj,year):
    count=0
    total_enrollments=0
    for course in courses:
        if course[0]==subj:
            count += 1
            total_enrollments += int(course[-1])
    print(subj,'had',count,'courses, enrolling',total_enrollments,\
          'average class size was',total_enrollments/count)

