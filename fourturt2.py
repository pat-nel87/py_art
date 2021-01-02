import turtle

turtle.title("A Tale of Four Turtles")

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
turtle.bgcolor("yellow")

boole = turtle.Turtle()
boole.color("red")
boole.shape("turtle")

pascal = turtle.Turtle()
pascal.color("blue")
pascal.shape("turtle")

feynman = turtle.Turtle()
feynman.color("green")
feynman.shape("turtle")

mandelbrot = turtle.Turtle()
mandelbrot.color("purple")
mandelbrot.shape("turtle")

boole.pendown()
pascal.pendown()
feynman.pendown()
mandelbrot.pendown()

for x in range (1,1000000000):
    if x % 2 == 0:
        boole.setheading(x*70)
        boole.forward(x+1)
        boole.speed(5*x)
        if boole.pos() == pascal.pos():
            boole.backward(x*2)
        feynman.setheading(x*120)
        feynman.speed(3/x)
        feynman.backward(x-1)
    elif x % 3 == 0:
        pascal.setheading(x*33)
        pascal.forward(x+1)
        mandelbrot.setheading(x*9)
        mandelbrot.backward(x-1)