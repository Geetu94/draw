

import turtle
def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(200)
        some_turtle.right(90)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(6)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    angie = turtle.Screen()
    angie.shape("turtle")
    angie.color("blue")
    angie.speed(5)
    angie.pensize(2)
    size=1
    while (True):
        angie.forward(size)
        angie.right(91)
        size = size + 1
draw_art()