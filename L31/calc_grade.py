'''
this program calculates your grade in CS10a
The grading criteria are as follows:

To earn a grade in the C range (C-, C, C+) 
 you must pass all of the weekly quiz questions, 
 at least 50% of the T&D skills, 
 and at least 3 PAs.

To earn a grade in the B range 
 you must pass all of the weekly quiz questions, 
 at least 70% of the T&D skills, 
 and at least 4 PAs.

To earn a grade in the A range 
 you must pass all of the weekly quiz questions, 
 at least 90% of the T&D skills, 
 and at least 5 PAs
'''
def print_grade_criteria(q_max,t_max,pa_max):
    print('-'*40)
    print('if you don\'t master all quizzes you get a D at most')
    print('otherwise,')
    print('to get an A you need ',end=" ")
    print('q=',q_max,'t>=',math.floor(0.9*t_max),'pa>=',pa_max)
    print('to get a B you need ',end=' ')
    print('q=',q_max,'t>=',math.floor(0.7*t_max),'pa>=',pa_max-1)
    print('to get a C you need ',end=' ')
    print('q=',q_max,'t>=',math.floor(0.5*t_max),'pa>=',pa_max-2)
    print('to get a D you need ',end=' ')
    print('q>=',q_max//2,'t>=',math.floor(0.3*t_max),'pa>=',pa_max-3)
    print('you get a E if', end=' ')
    print('q<',q_max//2,' or t<',math.floor(0.3*t_max),' or pa<',pa_max-3)
    print('-'*40)

import math
def print_letter_grade(q,t,pa,q_max=7, t_max=16, pa_max=3):
    grade = ""
    if q<q_max:
        print("you need to submit regrade requests on",
              q_max-q,'quizzes to pass the course')
    if t>=math.floor(0.9*t_max) and pa>=pa_max:
        grade = 'A'
    elif t>= math.floor(0.7*t_max) and pa>=pa_max-1:
        grade = 'B'
    elif t>= math.floor(0.5*t_max) and pa>= pa_max-2:
        grade = 'C'
    else:
        grade = 'D or E'
    print('-'*40)
    print('assuming you master all of the quiz questions')
    print('your grade based on T&Ds and Programming Assignments is',grade)

def calc_grade():
    

    print('go to the MLA sites')
    print('for quizzes (pin=6693852)')
    print('programming assignments (pin=202065)')
    print('T&Ds (pin= 9208539)')
    print('and the participation site (pin = 2970468)')
    print('take note of the number of skills on the main page')
    print('and the number of skills you\'ve mastered')
    print('also go to the participation MLA site')


    q_max = int(input("How many quizzes have their been? "))
    q = int(input("How many quiz skills have you mastered? "))
    t_max = int(input("how many T&D skills are there? "))
    t = int(input("and how many have you mastered? "))
    pa_max = float(input("How many Programming Assignments are there? "))
    print('note that program 2 has four parts each worth 0.25')
    pa = float(input("and how many have you mastered? "))
  
    print_grade_criteria(q_max,t_max,pa_max)
    print_letter_grade(q,t,pa,100-part,q_max, t_max, pa_max)
    print('your participation in class and your Spinoza problems')
    print('will determine the sign of your grade (i.e. B+ vs B vs B-)')

#calc_grade()
more='n'
while more=='y':
    q=int(input('q: '))
    t = int(input('t: '))
    p = float(input('p: '))
    print_letter_grade(q,t,p)
    print_grade_criteria(7,16,3)
    more = input('more? (y or n) ')

print('*'*30)
print_grade_criteria(10,20,5)