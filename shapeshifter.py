import turtle

turtle.title("Turtles, circles, colors!")
window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
euler = turtle.Turtle()  # A good mathy name for our turtle
euler.shape("circle")
scale = 3.14  # This isn't a turtle module setting.  This is just for us.

# Move the little buddy over to the left side to give him more room to work
euler.penup()
euler.setpos(-390, 0)
euler.pendown()
colors = ["red", "green", "purple", "black"]
bgcolors = ["blue", "yellow", "orange"]
current = 0   # Here's how we know where we are
seen = set()  # Here's where we'll keep track of where we've been


for each_color in colors:
# Step increases by 1 each time
    for step_size in range(1, 100):

        backwards = current - step_size

    # Step backwards if its positive and we've never been there before
        if backwards > 0 and backwards not in seen:
            euler.setheading(90)  # 90 degrees is pointing straight up
        # 180 degrees means "draw a semicircle"
            for each_bgcolor in bgcolors:
                for each_color in colors:
                    turtle.bgcolor(each_bgcolor)
                    euler.shape("triangle")
                    euler.color(each_color)
                    euler.circle(scale * step_size/2, 180)
                    euler.shapesize(10,10,10)
                    current = backwards
                    seen.add(current)
        elif backwards % 2 == 0:
            euler.shapesize(20,20,20)
            euler.shapesize(15,15,15)
            euler.shapesize(20,10,5)
            euler.shape("square")
            euler.penup()
            euler.setpos(-39, 0)
            euler.pendown()
    # Otherwise, go forwards
        else:
            euler.setheading(270)  # 270 degrees is straight down
            euler.shape("turtle")
            euler.shapesize(5,5,5)
            euler.color(each_color)
            euler.circle(scale * step_size/2, 180)
            current += step_size
            seen.add(current)

    turtle.done()

