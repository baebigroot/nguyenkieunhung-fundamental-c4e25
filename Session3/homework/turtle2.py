from turtle import *
colors =  ['red','blue','brown','yellow','gray']

for i in range(len(colors)):
    fillcolor(colors[i])
    pencolor(colors[i])
    for j in range(2):
        begin_fill()
        forward(30)
        left(90)
        forward(60)
        left(90)
        end_fill()
    forward(30)