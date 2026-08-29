# Very Simple Calculator

name = input('Your name: ')
print(f"Dear {name.title()}, Welcome to Simple Calculator.\n If you want  calculate something write numbers")
#symbol = input('Write there(+, -, *, /) : ')
score = []
bir_son = float(input('Enter first number: '))
ikki_son = float(input('Enter second number: '))
symbol = input('Write there(+, -, *, /) : ')
if symbol == '+':
    score = bir_son + ikki_son
elif symbol == '-':
    score = bir_son - ikki_son
elif symbol == '*':
    score = bir_son * ikki_son
elif symbol == '/' or symbol == ':' :
    score =   bir_son /  ikki_son
else:
    print('Wrong!')
print(f"Your score is =>  {score}")









