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


def draw_line(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0],p1[1]
    x2, y2 = p2[0],p2[1]

    for i in range (0, 100, 10): # range 는 정수밖에 들어가지 않기 때문에
        t = i / 100 # t는 0부터 1까지이다
        # x = 100 * (1-t**2)/(1+t**2)
        # y = 100 * 2*t/(1+t**2)
        x = t*x1 + (1-t)*x2
        y = t*y1 + (1-t)*y2
        draw_point((x,y))

    draw_point((x1,y1)) # 마지막에도 점을 정확하게 찍기 위해서

prepare_turtle_canvas()


# fill here
# points = [(-300, 200),(400, 350),(300, -300), (-200, -200)]
points = [(random.randint(-300, 300), random.randint(-300, 300)) for i in range(10)]
# 10개의 random list

for p in points:
    draw_big_point(p)

for i in range(0, len(points)-1):
    draw_line(points[i], points[i+1])
draw_line(points[-1], points[0]) # 마지막 점과 처음 점을 이어준다

turtle.done()