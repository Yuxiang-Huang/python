import turtle

def koch_curve(t, depth, length, scale_factor=1):
    if depth == 0:
        t.fd(length)
    else:
        koch_curve(t, depth-1, length * scale_factor, scale_factor)
        t.lt(60)
        koch_curve(t, depth-1, length * scale_factor, scale_factor)
        t.rt(120)
        koch_curve(t, depth-1, length * scale_factor, scale_factor)
        t.lt(60)
        koch_curve(t, depth-1, length * scale_factor, scale_factor)
        

michelangelo = turtle.Turtle()

def demo0(michelangelo):
    for i in range(3):
        michelangelo.pu()
        michelangelo.setx(-300)
        michelangelo.sety(300 - (i*300))
        michelangelo.pd()
        koch_curve(michelangelo, i, 100)

def demo1(michaelangelo):
    michelangelo.pu()
    michelangelo.speed(0)
    michelangelo.setx(-600)
    michelangelo.pd()
    koch_curve(michelangelo, 5, 200, scale_factor=.5)

demo0(michelangelo)
#demo1(michelangelo)


window = turtle.Screen()
window.exitonclick()