#Ex 1:
def hello():
    for i in range(3):
        print("Hello world")

hello()

#Ex 2:
def sum(x, y):
    s = x + y 
    print(s)

sum(7, 8)

#Ex 3:
from turtle import *

def draw_square(length, color):
    pencolor(color)
        
    for i in range(4):
            forward(length)
            left(90)

draw_square(100, "yellow")

#Ex 4:
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

#Ex 5:
from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    
    for i in range(5):
        right(144)
        forward(length)

draw_star(20, 100, 100)

#Ex 6:
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

        



