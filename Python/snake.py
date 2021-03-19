"""
Agustín Pumarejo A01028997
Sebastián Buendía A01027761
Santiago Cano A01029164

Agustín - Fixed the issue where the snake can turn 180°
Sebastián - Changed the color of the snake

"""

from turtle import *
from random import choice
from random import randrange
from freegames import square, vector

food= vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    #Added a condition for checking if the snake is only one block long, in which case it can move everywhere
    if len(snake) > 1:
        #Here the direction the snake is aiming can´t be changed 180° so the snake doesn´t crash onto itself right away
        if snake[-1] + vector(x, y) != snake[-2]:
            aim.x = x
            aim.y = y
    else:
        aim.x = x
        aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    global food
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    food_check = vector(0,0)
# Se creo un loop el cual compara las cordenadas de la comida y verifica que no esten dentro de la serpiente, 
# asi evitando comida que aparezca dentro de la serpente.
    if head == food:
        print('Snake:', len(snake))
        while food_check in snake:
            x1=randrange(-15, 15) * 10
            y1= randrange(-15, 15) * 10
            food_check = vector(x1,y1)
        food=food_check   
    else:
        snake.pop(0)

    clear()
# Se importo la funcion choice de una libreria y se uso en el color,
# creando una variable con colores se hizo que la sepriente fuera de varios colores cambiando conforme el tiempo
    colors_f=['cyan','blue','Dark violet','black','chocolate']
    for body in snake:
        square(body.x, body.y, 9,choice(colors_f))
        

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
