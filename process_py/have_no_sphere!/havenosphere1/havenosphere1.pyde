def setup():
     size(1200,1200, P3D)
     background(0,0,0)
    
def draw():
    
    i = 0
    if mousePressed:
       directionalLight(mouseX,mouseY,mouseX+mouseY,0,0,-1)
       ambientLight(mouseX, mouseY, 5)
       for i in range(1, 100): 
           r = random(mouseX)
           fill(mouseY, 255, r)           
           
           sphere(r)
           translate(mouseY, mouseX, mouseX)
           
           fill(mouseX, 0, 238)    
           sphere(r)
           translate(mouseY, mouseX, mouseX)
           i += i
    else:
        background(0,0,0)
        r = random(300)
        fill(r,255,0)
        ambientLight(mouseX, mouseY, 5)
        translate(mouseX, mouseY, mouseY)
        sphere(75)
        translate(mouseY, mouseX, mouseX)
        sphere(75)
