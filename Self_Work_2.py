# QUIZ TEST

name = input('Name: ')
#taker_0['ism'] = name
print(f"Hi, {name}. Welcome to Quiz tests.\nIf you want to test yourself about anything. You make right decision")
#ok

math_1 = '2+22\nA.24  B.20'
math_2 = 'x+9=25 x=\nA.14  B.16 '
math_3 = '16+x=41 x=?\nA.25 B.15  C.31  D.20'
math_4 = '4*x=88 x=?\nA.22  B.24  C.20  D.12'
math_5 = '15*x=60 x=?\nA.4  B.6  C.8  D.2'
math_6 = '(4+x)+15 = 75 x=?\nA.5  B.15  C.20  D.10'
math_7 = '965+25-84 = ?\nA.9006  B.805  C.906  D.IDK' #C
math_8 = 'x+45-21*(455+456-453-400+2-59) = 27\nA.3 B.21 C.4 D.2'  #A


english_1 = 'pass __ \nA.out  B.yourself'
english_2 = 'bumb__\nA.your head  B.your ankle'
english_3 = ''

print('''
|
|
|
|
|
We have math and english tests''')
choose = input('Choose from them: ')

#Math
if choose.title() == 'Math' or choose.title() == 'Mathematic' :
    print('''You chose Math
    
    
    ''')

    score = []
    length = 0


    print(f'1. {math_1}')
    q1 = input('Answer: ')
    print(f'2. {math_2}')
    q2 = input('Answer: ')
    print(f'3. {math_3}')
    q3 = input('Answer: ')
    print(f'4. {math_4}')
    q4 = input('Answer: ')
    print(f'5. {math_5}')
    q5 = input('Answer: ')
    print(f'6. {math_6}')
    q6 = input('Answer: ')

    if q1.upper() == 'A':
        score.append(f'1.{q1.upper()} (True) ')
        length = length + 1
    elif q1.upper() != 'A':
        score.append(f'1.{q1.upper()} (False)')
    if q2.upper() == 'B':
        score.append(f'2.{q2.upper()} (True)')
        length = length + 1
    elif q2.upper() != 'B':
        score.append(f'2.{q2.upper()} (False)')

    if q3.upper() == 'A':
        score.append(f'3.{q3.upper()} (True) ')
        length = length + 1
    elif q3.upper() != 'A':
        score.append(f'3.{q3.upper()} (False)')

    if q4.upper() == 'A':
        score.append(f'4.{q4.upper()} (True)')
        length = length + 1
    elif q4.upper() != 'A':
        score.append(f'4.{q4.upper()} (False)')

    if q5.upper() == 'A':
        score.append(f'5.{q5.upper()} (True) ')
        length = length + 1
    elif q5.upper() != 'A':
        score.append(f'5.{q5.upper()} (False)')

    if q6.upper() == 'B':
        score.append(f'6.{q6.upper()} (True)')
        length = length + 1
    elif q6.upper() != 'B':
        score.append(f'6.{q6.upper()} (False)')

    if q5.upper() == 'A':
        score.append(f'5.{q5.upper()} (True) ')
        length = length + 1
    elif q5.upper() != 'A':
        score.append(f'5.{q5.upper()} (False)')

    if q6.upper() == 'B':
        score.append(f'6.{q6.upper()} (True)')
        length = length + 1
    elif q6.upper() != 'B':
        score.append(f'6.{q6.upper()} (False)')

    print(score)
    print(f"Youn found {length} correct answer(s) from math tests")



#English Test

elif choose.title() == 'English':
    print('You chose English')
    print('''Start>>>
    
    ''')
    score = []
    length = 0

    #questions
    print(f'1. {english_1}')
    e1 = input('Answer: ')
    print(f'2.{english_2}')
    e2 = input('Answer: ')

    #checking
    if e1.upper() == 'A':
        score.append(f'1.{e1.upper()} (True) ')
        length = length + 1
    elif e1.upper() != 'A':
        score.append(f'1.{e1.upper()} (False)')
    if e2.upper() == 'A':
        score.append(f'2.{e2.upper()} (True)')
        length = length + 1
    elif e2.upper() != 'A':
        score.append(f'2.{e2.upper()} (False)')
    print(score)
    print(f"Youn found {length} correct answer(s) from english tests")


# Error

else :
    print('''Choose from these
    Error has ocurred
    Please try again later''')



'''

Developer Ahliddin
Name: Quiz Test
Version: 2026.1.1
Facilities: Give a test about math and english
Main Goal: don't need to write each question or answer inside 'if-else'
Opportunity: can write questions before 'if-else' with integer
Update: every day

Copyright Ahliddin
'''