# Animation Example

time = 0   # use time to move objects from one frame to the next

def setup():
    size (700, 700, P3D)
    perspective (60 * PI / 180, 1, 0.1, 2000)  # 60 degree field of view
    
def draw():
    global time
    if time < 10:
        time += 0.01
    100 + time*50
    camera (100 - 40*time, -100 + 5*time, 100 + time*50, 0, 0, time*35, 0, 1, 0)  # position the virtual camera

    # camera (0, -600, 750, 0, 0, 0, 0, 1, 0)
    # camera (0, -600, -600+200*time, 0, 0, 0, 0, 1, 0)

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(100, 100, 100);
    lightSpecular(100, 100, 100)
    directionalLight (200, 200, 200, -0.3, 0.5, -1)
    
    noStroke()
    specular (255, 255, 255)
    shininess (5.0)

    bmo(0,0,40*time)
    forest()
    ground()
    
def forest():
    tree(-100,0,0,30)
    tree(-220,0,-69,40)
    tree(-127,0,100,50)
    tree(-87,0,224,60)
    tree(-192,0,380,52)
    tree(141,0,111,25)
    tree(150,0,35,65)
    tree(204,0,406,43)
    tree(89,0,209,42)

def tree(x,y,z,big, sides = 64):
    fill(0,175,0)
    pushMatrix()
    translate(x,y,z)
    scale(big,big,big)
    translate(0,-0.5,0)
    pushMatrix()
    translate(0,-1,0)
    rotateX(radians(90))
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (0, 0, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (0, 0, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
    popMatrix()
    fill(75,0,0)
    pushMatrix()
    translate(0,-0.4,0)
    scale(0.2,1,0.2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    popMatrix()
    
def ground():
    fill(45,10,30)
    pushMatrix()
    rotateX(radians(90))
    scale(5,5,5)
    beginShape()
    vertex(50,100,0)
    vertex(50,-20,0)
    vertex(-50,-20,0)
    vertex(-50,100,0)
    endShape(CLOSE)
    popMatrix()

def bmo(x,y,z):
    pushMatrix()
    translate(x,y,z)
    pushMatrix()
    translate(0,-17,0)
    pushMatrix()
    body()
    popMatrix()
    pushMatrix()
    translate(0,-23,7.6)
    face()
    popMatrix()
    popMatrix()
    popMatrix()
               
# basic body (no face/drawings)
def body():
    rate = 5 * time
    pushMatrix()
    translate(0,-17,0)
    base()
    popMatrix()
    pushMatrix()
    translate(-8,0,0)
    z = sin(5*time)
    translate(0,0,-3*z)
    leg()
    popMatrix()
    pushMatrix()
    translate(8,0,0)
    z1 = sin(5*time)
    translate(0,0,3*z1)
    leg()
    popMatrix()
    pushMatrix()
    translate(15,-8,0)
    rotateX(-5*time)
    armR()
    popMatrix()
    pushMatrix()
    translate(-15,-8,0)
    rotateX(-5*time)
    armL()
    popMatrix()
    pushMatrix()
    translate(5,-3.5,8)
    cirButton1()
    popMatrix()
    pushMatrix()
    translate(9,-7.5,8)
    cirButton2()
    popMatrix()
    pushMatrix()
    translate(3,-7,8)
    scale(0.9,0.9,1)
    triButton()
    popMatrix()
    pushMatrix()
    translate(-7.5,-7,8)
    scale(1.2,1.2,1)
    crossT()
    popMatrix()
    pushMatrix()
    translate(-9.5,-3,8)
    scale(0.7,0.9,1)
    bar()
    popMatrix()
    pushMatrix()
    translate(-5.5,-3,8)
    scale(0.7,0.9,1)
    bar()
    popMatrix()
    
# face (hope it comes out)
def face():
    # stroke(255)
    fill(20, 170, 130)
    beginShape()
    vertex(11,-8,0)
    vertex(-11,-8,0)
    vertex(-11,8,0)
    vertex(11,8,0)
    endShape(CLOSE)
    fill(0)
    pushMatrix()
    translate(-5,-1,0)
    scale(0.75,0.75,0.15)
    translate(0,0,1)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(5,-1,0)
    scale(0.75,0.75,0.15)
    translate(0,0,1)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(0,0.5,-.99)
    scale(2.5,1.5,1)
    beginShape()
    for i in range(17):
        theta = i * 2 * PI / 32
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    popMatrix()
    

# mini bar button
def bar():
    fill(10,0,0)
    pushMatrix()
    translate(-1.5,0,0)
    scale(0.5,0.5,0.25)
    cylinder()
    popMatrix()
    pushMatrix()
    translate(1.5,0,0)
    scale(0.5,0.5,0.25)
    cylinder()
    popMatrix()
    pushMatrix()
    scale(3,1,0.5)
    box(1)
    popMatrix()
    
# yellow cross button
def crossT():
    fill(200,180,0)
    pushMatrix()
    scale(4/3,4/3,1)
    pushMatrix()
    scale(3,1,0.5)
    box(1)
    popMatrix()
    pushMatrix()
    scale(1,3,0.5)
    box(1)
    popMatrix()
    popMatrix()
    
# red circle button
def cirButton1():
    fill(255,0,0)
    pushMatrix()
    scale(2.5,2.5,0.25)
    cylinder()
    popMatrix()
    
# green circle button (smaller)
def cirButton2():
    fill(0,255,0)
    pushMatrix()
    scale(1.5,1.5,0.25)
    cylinder()
    popMatrix()

# triangle button
def triButton():
    pushMatrix()
    scale(2,2,0.5)
    tri()
    popMatrix()
    
def tri():
    fill (0,0,255)
    beginShape()
    vertex(-1, 0, 1)
    vertex(1, 0, 1)
    vertex(0,-sqrt(3),1)
    endShape(CLOSE)
    beginShape()
    vertex(-1, 0, -1)
    vertex(1, 0, -1)
    vertex(0,-sqrt(3),-1)
    endShape(CLOSE)
    beginShape()
    vertex(-1, 0, 1)
    vertex(-1, 0, -1)
    vertex(0,-sqrt(3),-1)
    vertex(0,-sqrt(3),1)
    endShape(CLOSE)
    beginShape()
    vertex(1, 0, 1)
    vertex(1, 0, -1)
    vertex(0,-sqrt(3),-1)
    vertex(0,-sqrt(3),1)
    endShape(CLOSE)
    beginShape()
    vertex(-1, 0, 1)
    vertex(-1, 0, -1)
    vertex(1, 0, -1)
    vertex(1, 0, 1)
    endShape(CLOSE)
# leg
def leg():
    fill(0, 130, 120)
    pushMatrix()
    scale(2,7.5,2)
    translate(0,1,0)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    pushMatrix()
    translate(0,15,-3)
    scale(2.2,2,4)
    translate(0,1,1)
    box(2)
    popMatrix()
    
# arm: cylinders
def armL():
    pushMatrix()
    rotateY(radians(180))
    arm()
    popMatrix()
    pushMatrix()
    translate(-10.5,0,0)
    rotateZ(radians(-55))
    rotateY(radians(180))
    arm()
    popMatrix()
    
def armR():
    pushMatrix()
    arm()
    popMatrix()
    pushMatrix()
    translate(10.5,0,0)
    rotateZ(radians(-55))
    arm()
    popMatrix()

def arm():
    fill(0, 130, 120)
    pushMatrix()
    # rotateX(time)
    scale(6,2,2)
    translate(1,0,0)
    rotateY(radians(90))
    cylinder()
    popMatrix()

# body base
def base():
    fill(0, 140, 100)
    pushMatrix()
    # rotateY(time)
    scale(3.0, 3.5, 1.5) 
    box(10)
    popMatrix()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2