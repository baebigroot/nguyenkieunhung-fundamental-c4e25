from random import *
from calc import eval

def generate_quiz():
    x = randint(0,20)
    y = randint(0,20)

    error = randint(-3,3)

    op = choice(["+", "-", "*", "/"])

    result = eval(x, y, op) + error

    return [x, y, op, result]
   

def check_answer(x, y, op, result, user_choice):
    correct = eval(x, y, op)
    if correct == result:
        if user_choice == True:
            check = True
        else:
            check = False
    else:
        if user_choice == True:
            check = False
        else:
            check = True

    return check


        

