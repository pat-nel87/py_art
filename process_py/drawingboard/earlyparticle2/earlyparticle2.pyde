def setup():
     size(1200,1200)
     background(0,0,0)

def draw():
    i = 0
    if mousePressed:
       for i in range(1, 100): 
           fill(102, 255, 0)
           circle(mouseX*i, mouseY*i, i)
           
           fill(255, 0, 238)
           circle(mouseY*i, mouseX*i, i*2)
           i += i
    else:
        fill(255,255,0)
        strokeWeight(4)
        beginShape()
        vertex(mouseX, mouseY)
        quadraticVertex(mouseY, mouseX-mouseY, mouseX+mouseX, mouseY)
        quadraticVertex(mouseX,mouseY, mouseX, mouseY)
        vertex(mouseY, mouseX)
        endShape()
           
