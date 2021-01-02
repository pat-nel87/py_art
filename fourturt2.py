import turtle

turtle.title("Advanced Turtlenometry")

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
turtle.bgcolor("black")

boole = turtle.Turtle()
boole.color("red")
boole.shape("turtle")

pascal = turtle.Turtle()
pascal.color("yellow")
pascal.shape("turtle")

feynman = turtle.Turtle()
feynman.color("green")
feynman.shape("turtle")

mandelbrot = turtle.Turtle()
mandelbrot.color("orange")
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

        feynman.setheading(x*120)
        feynman.speed(3/x)
        feynman.circle(x)
        feynman.backward(x-1)
    elif x % 3 == 0:
        pascal.setheading(x*33)
        pascal.forward(x+1)
        mandelbrot.setheading(x*9)
        mandelbrot.speed(x*3.14)
        mandelbrot.circle(x*3.14)

        mandelbrot.backward(x-1)