import turtle
import random

def tree_standard(t, depth, size, angle):
    if depth == 0:
        t.fd(size)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(angle)
        tree_standard(t, depth-1, size, angle)
        t.lt(2 * angle)
        tree_standard(t, depth-1, size, angle)
        t.rt(angle)
        t.bk(size)

def tree(t, depth, size, angle, width):
    t.width(width)
    if depth == 0:
        t.pencolor("green")
        t.fd(size)
        t.bk(size)
    else:
        t.pencolor("brown")
        angle+= random.randrange(-5, 5)
        size+= random.randrange(-5, 5)
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size * .75, angle, width-1)
        t.lt(2 * angle)
        tree(t, depth-1, size * .75, angle, width-1)
        t.rt(angle)
        t.bk(size)
        
        
donatello = turtle.Turtle()
donatello.lt(90)
donatello.speed(0)

tree(donatello, 10, 150, 20, 11)





window = turtle.Screen()
window.exitonclick()