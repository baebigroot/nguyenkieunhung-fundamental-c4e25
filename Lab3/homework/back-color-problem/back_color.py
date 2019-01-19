from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(["BLUE","RED","YELLOW","GREEN"]),
                choice(["#3F51B5","#C62828","#FFD600","#4CAF50"]),
                randint(0, 1)
            ]
def is_inside(x,y):
    if(y[0]<x[0]<y[0]+y[2]) and (y[1]<x[1]<y[1]+y[3]):
        return True
    else:
        return False

def mouse_press(x, y, text, color, quiz_type):
    for check in shapes:
        if quiz_type == 0:
            if check['color'] == color:
                click = inside([x, y], check['rect'])
        else:
            if check['text'] == text.lower():
                click = inside([x, y], check['rect'])
    return click
