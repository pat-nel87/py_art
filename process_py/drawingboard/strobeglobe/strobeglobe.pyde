def setup():
     size(1200,1200, P3D)
     background(0,0,0)
     directionalLight(mouseX,mouseY,mouseX+mouseY,0,0,-1)
def draw():
    
    i = 0
    if mousePressed:
       for i in range(1, 100): 
           r = random(300)
           fill(mouseY, 255, 0)           
           sphere(r)
           
           
           fill(mouseX, 0, 238)    
           sphere(r)
           i += i
    else:
        r = random(300)
        fill(r,255,0)
        ambientLight(mouseX, mouseY, 5)
        translate(mouseX, mouseY, mouseY)
        sphere(mouseX)
        translate(mouseY, mouseX, mouseX)
        sphere(mouseY)
