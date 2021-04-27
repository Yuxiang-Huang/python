import turtle

def draw_spiral0(t, length):
    min_length = 5
    while length > min_length:
        t.fd(length)
        t.rt(90)
        length-= min_length





def draw_spiral(t, length):

    min_length = 5
    if length > min_length:
        t.fd(length)
        t.rt(90)
        draw_spiral(t, length - min_length)

donatello = turtle.Turtle()
#donatello.speed(8)

draw_spiral(donatello, 200)


window = turtle.Screen()
window.exitonclick()