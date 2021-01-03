def setup():
    size(1480, 820)

def draw():
    if  mousePressed:
        fill(0)
        noFill()
    bezier(85, 20, 10, 10, 90, 90, 15, 80)
    steps = 6
    fill(255)
    for i in range(steps + 1): 
        t = i / float(steps)
        # Get the location of the point
        x = bezierPoint(85, 10, 90, 15, t)
        y = bezierPoint(20, 10, 90, 80, t)
        # Get the tangent points
        tx = bezierTangent(85, 10, 90, 15, t)
        ty = bezierTangent(20, 10, 90, 80, t)
        # Calculate an angle from the tangent points
        a = atan2(ty, tx)
        a += PI
        stroke(255, 102, 0)
        line(x, y, cos(a)*30 + x, sin(a)*30 + y)
        # The following line of code makes a line 
        # inverse of the above line
        #line(x, y, cos(a)*-30 + x, sin(a)*-30 + y)
        stroke(0)
        ellipse(x, y, 5, 5)
    else:
        noFill()
        stroke(255, 102, 0)
        stroke(0, 0, 0)
        bezier(mouseX, mouseY, mouseX-mouseY, mouseY+mouseY, mouseY+mouseX, mouseX+mouseX, mouseY, mouseX)
