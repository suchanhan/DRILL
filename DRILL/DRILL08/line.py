import turtle
import random
import math


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


# 직선의 방정식
def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    a = (y2 - y1)/(x2 - x1)
    b = y1 - a * x1

    for x in range(x1, x2+1, 10):
        y = a*x+b
        draw_point((x,y))

    draw_point(p2)
    pass


def draw_line(p1, p2):

    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 314, 1):
        t = i/10
        a = 160
        b = 100
        x = (a-b)*math.cos(t) + b*math.cos(t*(a/b-1))
        y = (a-b)*math.sin(t) - b*math.sin(t*(a/b-1))
        draw_point((x, y))

    draw_point(p2)
    pass


prepare_turtle_canvas()

p1 = (200, 200)
p2 = (300, 300)


draw_line(p1, p2)

turtle.done()