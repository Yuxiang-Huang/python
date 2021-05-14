import turtle

def draw_square(t, length):
    i = 0
    while i < 4:
        t.fd(length)
        t.rt(90)
        i+= 1


def draw_spiral0(t, length):
    min_length = 5
    while length > min_length:
        t.fd(length)
        t.rt(90)
        length -= min_length

def draw_spiral1(t, length, angle):
    min_length = 5
    while length > min_length:
        t.fd(length)
        t.rt(angle)
        length-= min_length


donatello = turtle.Turtle()
donatello.speed(8)

#draw_square(donatello, 100)
#draw_spiral0(donatello, 200)
draw_spiral1(donatello, 200, 30)


window = turtle.Screen()
window.exitonclick()