from turtle import *
import turtle
import time

friction = 5
acceleration = 3
limiteVitesse = 30
MarioScale = 10
gravite = 5


onGround = True
inJump = False
MarioAnimation = 0
MarioCooldown = False
MarioCooldownCounter = 0
AnimeSpeed = 2
ground = -348
VitesseX = 1
VitesseY = 0
position = "Forward"
endGame = False
isWalking = False
isJumping = False
downwPos = 1.0, -348.01
forwPos = 1.0, 1.0
screen = turtle.Screen()
b = turtle.Turtle()
m = turtle.Turtle()
width(4)
speed(5)



#all def
def terre():
    down()
    color("Black")
    width(3)
    
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    color("DarkOrange4")
    end_fill()

    width(3)
    def craks():
        XY = pos()
        left(90)
        justMove(25)
        right(90 + 15)
        forward(53.8516)
        left(15)
        right(90)   
        forward(10)
        left(180)
        justMove(5)
        right(15)
        forward(70.178344)
        left(15)
        forward(25)
        left(180)
        justMove(25)
        left(90)
        forward(25)
        right(90)
        justMove(74)
        right(90)
        justMove(95)
        left(180)
        goto(*XY)
    color("white")
    craks()
    color("black")
    justMove(3)
    craks()
    left(180)
    justMove(3)
    left(180)


def justMove(steps):
    up()
    forward(steps)
    down()

def mjustMove(steps):
    m.up()
    m.forward(steps)
    m.down()

def bjustMove(steps):
    b.up()
    b.forward(steps)
    b.down()

def blocSpecial():
    down()
    color("Black") #basic cube
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    color("DarkGoldenrod1")
    end_fill()

    def TheSymbol():
        justMove(30) 
        left(90)
        justMove(55)
        width(10)
        for i in range(3):
            forward(20)
            justMove(10)
            right(90)
            justMove(10)
        left(90)
        forward(10)
        right(90)
        justMove(5)
        left(90)
        forward(7)
        justMove(15)
        forward(3)
        up()
   
    color("Black") #allsymbol
    justMove(5)
    TheSymbol()
    justMove(10)
    right(90)
    justMove(60)
    left(180)
    color("DarkGoldenrod4")
    TheSymbol()
    
    justMove(10)
    left(90)
    left(180)
    justMove(55)
    left(180)
    up()

def bush():
    b.down()
    b.color("black")
    BXY = b.pos()
    Birection = b.heading()
    b.left(55)
    b.begin_fill()
    b.forward(50)
    b.left(35)
    b.forward(20)
    b.right(90)
    b.forward(20)
    b.left(55)
    b.forward(20)
    for i in range(11):
        b.forward(4)
        b.right(10)
    b.forward(20)
    b.left(55)
    b.forward(20)
    b.right(90)
    b.forward(20)
    b.left(35)
    b.forward(50)
    b.goto(*BXY)
    b.color("chartreuse")
    b.end_fill()
    b.setheading(Birection)

def brique():
    down()
    width(3)
    color("black")
    begin_fill()
    for i in range(4): #p'tit trait
        forward(100)
        left(90)
    color("DarkOrange4")
    end_fill()
    color("black")
    justMove(25)
    left(90)
    for i in range(2):
        for i in range(2):
            justMove(25)
            forward(25)
        right(90)
        justMove(25)
        right(90)
    right(90)
    justMove(50)
    left(90)
    for i in range(2):
        justMove(25)
        forward(25)
    
    #ligne droite
    right(90)
    justMove(25)
    right(90)
    color("DarkOrange4")
    forward(25)
    color("black")
    right(90)
    forward(100)

    right(90)   #earase ligne
    color("DarkOrange4")
    forward(25)
    color("black")
    left(180)
    justMove(25)

    
    justMove(25)
    left(90)
    forward(100)

    right(90)
    color("DarkOrange4")
    forward(25)
    color("black")
    right(90)
    forward(100)

    right(90)    #earase ligne
    color("DarkOrange4")
    forward(25)
    color("black")
    left(180)
    justMove(25)

    #left(90)  #revenir a la position de depart
    justMove(25)
    left(90)


def MARIO(scale, Costume):
    m.down()
    mBasicPos = m.pos()
    m.width(1)
    def pixel(c):
        m.color(c)
        m.begin_fill()
        for i in range(4):
            m.forward(scale)
            m.left(90)
        m.end_fill()
        m.forward(scale)
    XYBase = m.pos()
    XYBase = list(XYBase)
    def XsetPos(Upp):
        m.up()
        XYBase[1] += Upp* (scale/Upp)
        m.goto(XYBase[0],XYBase[1])
        m.down()
    

    if Costume == 0:
        XsetPos(1)
        for i in range(4):
            pixel("Yellow4")
        mjustMove(scale*4)
        for i in range(4):
            pixel("Yellow4")
        
        XsetPos(2)
        mjustMove(scale)
        for i in range(3):
            pixel("Yellow4")
        mjustMove(scale*4)
        for i in range(3):
            pixel("Yellow4")
            
        
        XsetPos(3)
        mjustMove(scale*2)
        for i in range(3):
            pixel("red")
            
        mjustMove(scale*2)
        for i in range(3):
            pixel("red")
        
        XsetPos(4)
        for i in range(2):
            pixel("Goldenrod2")
        for i in range(8):
            pixel("red")
        for i in range(2):
            pixel("Goldenrod2")
        
        XsetPos(5)
        for i in range(3):
            pixel("Goldenrod2")
        for i in range(6):
            pixel("red")
        for i in range(3):
            pixel("Goldenrod2")

        XsetPos(6)
        for i in range(2):
            pixel("Goldenrod2")
        pixel("Yellow4")
        pixel("Red")
        pixel("Goldenrod2")
        pixel("Red")
        pixel("Red")
        pixel("Goldenrod2")
        pixel("Red")
        pixel("Yellow4")
        for i in range(2):
            pixel("Goldenrod2")

        XsetPos(7)
        for i in range(4):
            pixel("Yellow4")
        pixel("red")
        for i in range(2):
            pixel("Yellow4")
        pixel("red")
        for i in range(4):
            pixel("Yellow4")

        XsetPos(8)
        mjustMove(scale)
        for i in range(3):
            pixel("Yellow4")
        pixel("red")
        for i in range(2):
            pixel("Yellow4")
        pixel("red")
        for i in range(3):
            pixel("Yellow4")

        XsetPos(8)
        mjustMove(scale*3)
        pixel("Yellow4")
        pixel("red")
        for i in range(3):
            pixel("Yellow4")
        
        XsetPos(9)
        mjustMove(scale*3)
        for i in range(7):
            pixel("Goldenrod2")
        
        XsetPos(10)
        mjustMove(scale)
        for i in range(2):
            pixel("Yellow4")
        for i in range(4):
            pixel("Goldenrod2")
        for i in range(4):
            pixel("Yellow4")

        XsetPos(11)
        mjustMove(scale)
        pixel("Yellow4")
        pixel("Goldenrod2")
        for i in range(2):
            pixel("Yellow4")
        for i in range(3):
            pixel("Goldenrod2")
        pixel("Yellow4")
        for i in range(3):
            pixel("Goldenrod2")

        XsetPos(12)
        mjustMove(scale)
        pixel("Yellow4")
        pixel("Goldenrod2")
        pixel("Yellow4")
        for i in range(3):
            pixel("Goldenrod2")
        pixel("Yellow4")
        for i in range(3):
            pixel("Goldenrod2")

        XsetPos(13)
        mjustMove(scale*2)
        for i in range(3):
            pixel("Yellow4")
        for i in range(2):
            pixel("Goldenrod2")
        pixel("Yellow4")
        pixel("Goldenrod2")

        XsetPos(14)
        mjustMove(scale*2)
        for i in range(9):
            pixel("red")
        
        XsetPos(15)
        mjustMove(scale*3)
        for i in range(6):
            pixel("red")
    
    if Costume == 1:
        XsetPos(1)
        mjustMove(MarioScale)
        for i in range(3):
            pixel("Yellow4")

        XsetPos(2)
        for i in range(3):
            pixel("Yellow4")

        XsetPos(3)
        for i in range(2):
            pixel("Yellow4")
        for i in range(3):
            pixel("red")
        for i in range(3):
            mjustMove(MarioScale)
        for i in range(3):
            pixel("red")
        for i in range(2):
            pixel("Yellow4")

        XsetPos(4)
        mjustMove(MarioScale)
        for i in range(10):
            pixel("red")
        for i in range(2):
            pixel("Yellow4")

        XsetPos(5)
        mjustMove(MarioScale*2)
        for i in range(9):
            pixel("red")
        for i in range(2):
            pixel("Yellow4")

        XsetPos(6)
        m.left(180)
        mjustMove(MarioScale)
        m.left(180)
        for i in range(2):
            pixel("Goldenrod2")
        mjustMove(MarioScale*2)
        for i in range(7):
            pixel("red")
        mjustMove(MarioScale*2)
        pixel("Yellow4")

        XsetPos(7)
        m.left(180)
        mjustMove(MarioScale)
        m.left(180)
        for i in range(3):
            pixel("Goldenrod2")
        mjustMove(MarioScale)
        for i in range(2):
            pixel("Yellow4")
        pixel("Red")
        pixel("Goldenrod2")
        for i in range(3):
            pixel("red")
        for i in range(2):
            pixel("Yellow4")
        for i in range(2):
            pixel("Goldenrod2")

        XsetPos(8)
        m.left(180)
        mjustMove(MarioScale)
        m.left(180)
        for i in range(2):
            pixel("Goldenrod2")
        for i in range(4):
            pixel("Yellow4")
        for i in range(3):
            pixel("red")
        for i in range(3):
            pixel("Yellow4")
        for i in range(3):
            pixel("Goldenrod2")
        
        XsetPos(9)
        mjustMove(MarioScale)
        for i in range(4):
            pixel("Yellow4")
        for i in range(2):
            pixel("red")
        for i in range(2):
            pixel("Yellow4")

        XsetPos(10)
        mjustMove(MarioScale*4)
        for i in range(7):
            pixel("Goldenrod2")

        XsetPos(11)
        mjustMove(MarioScale*2)
        for i in range(2):
            pixel("Yellow4")
        for i in range(4):
            pixel("Goldenrod2")
        for i in range(4):
            pixel("Yellow4")

        XsetPos(12)
        mjustMove(MarioScale*2)
        pixel("yellow4")
        pixel("goldenrod2")
        for i in range(2):
            pixel("Yellow4")
        for i in range(3):
            pixel("Goldenrod2")
        pixel("Yellow4")
        for i in range(3):
            pixel("Goldenrod2")
        
        XsetPos(13)
        mjustMove(MarioScale*2)
        pixel("yellow4")
        pixel("goldenrod2")
        pixel("yellow4")
        for i in range(3):
            pixel("goldenrod2")
        pixel("yellow4")
        for i in range(3):
            pixel("goldenrod2")

        XsetPos(14)
        mjustMove(MarioScale*3)
        for i in range(3):
            pixel("Yellow4")
        for i in range(2):
            pixel("goldenrod2")
        pixel("Yellow4")
        pixel("Goldenrod2")

        XsetPos(15)
        mjustMove(MarioScale*3)
        for i in range(9):
            pixel("red")
        
        XsetPos(16)
        mjustMove(MarioScale*4)
        for i in range(5):
            pixel("red")

    if Costume == 2:
        XsetPos(1)
        mjustMove(MarioScale*5)
        for i in range(3):
            pixel("yellow4")

        XsetPos(2)
        mjustMove(MarioScale*5)
        for i in range(6):
            pixel("yellow4")

        XsetPos(3)
        mjustMove(MarioScale*5)
        for i in range(2):
            pixel("red")
        for i in range(3):
            pixel("yellow4")

        XsetPos(4)
        mjustMove(MarioScale*4)
        pixel("red")
        pixel("yellow4")
        pixel("goldenrod2")
        for i in range(3):
            pixel("red")

        XsetPos(5)
        mjustMove(MarioScale*3)
        pixel("red")
        for i in range(2):
            pixel("yellow4")
        for i in range(2):
            pixel("goldenrod2")
        for i in range(3):
            pixel("red")

        XsetPos(6)
        mjustMove(MarioScale*3)
        for i in range(3):
            pixel("yellow4")
        for i in range(5):
            pixel("red")

        XsetPos(7)
        mjustMove(MarioScale*3)
        for i in range(3):
            pixel("yellow4")
        pixel("red")
        pixel("goldenrod2")
        for i in range(2):
            pixel("red")
        pixel("goldenrod2")

        XsetPos(8)
        mjustMove(MarioScale*3)
        for i in range(3):
            pixel("yellow4")
        for i in range(2):
            pixel("red")
        for i in range(2):
            pixel("yellow4")

        XsetPos(9)
        mjustMove(MarioScale*4)
        for i in range(5):
            pixel("yellow4")

        XsetPos(10)
        mjustMove(MarioScale*5)
        for i in range(6):
            pixel("goldenrod2")

        XsetPos(11)
        mjustMove(MarioScale*3)
        for i in range(2):
            pixel("yellow4")
        for i in range(3):
            pixel("goldenrod2")
        for i in range(4):
            pixel("yellow4")

        XsetPos(12)
        mjustMove(MarioScale * 3)
        pixel("yellow4")
        pixel("goldenrod2")
        pixel("yellow4")
        for i in range(3):
            pixel("goldenrod2")
        pixel("yellow4")
        for i in range(3):
            pixel("goldenrod2")

        XsetPos(13)
        mjustMove(MarioScale * 3)
        pixel("yellow4")
        pixel("goldenrod2")
        pixel("yellow4")
        for i in range(2):
            pixel("goldenrod2")
        pixel("yellow4")
        for i in range(3):
            pixel("goldenrod2")

        XsetPos(14)
        mjustMove(MarioScale * 4)
        for i in range(2):
            pixel("yellow4")
        for i in range(2):
            pixel("goldenrod2")
        pixel("yellow4")
        pixel("goldenrod2")

        XsetPos(14)
        mjustMove(MarioScale * 4)
        for i in range(8):
            pixel("red")

        XsetPos(14)
        mjustMove(MarioScale * 5)
        for i in range(4):
            pixel("red")
    
    m.up()
    m.goto(mBasicPos)



def Walking():
    global isWalking, position
    isWalking = True

    if position == "Downward":
        mjustMove(MarioScale*10)
    position = "Forward"

    m.setheading(0)
    #m.sety(-348 - MarioScale)

def stepBack():
    global isWalking, position
    isWalking = True

    if position == "Forward":
        mjustMove(MarioScale*10)
    position = "Downward"

    m.setheading(180)
    #m.sety(-348 )

def stopWalking():
    global isWalking
    isWalking = False

def saut():
    global isJumping
    isJumping = True

def StopSaut():
    global isJumping
    isJumping = False




def GameLoop():
    global VitesseX, VitesseY, MarioAnimation, MarioCooldownCounter, MarioCooldown, ground, inJump, onGround
    #Updating variable
    xPos = m.pos()[0]
    yPos = m.pos()[1]

    



    #checkAction

    if position == "Forward":
        ground = -348 - MarioScale
        if isWalking == True:
            if VitesseX < limiteVitesse:
                VitesseX += acceleration

        if isWalking == False:
            if VitesseX > 0:
                VitesseX -= friction
            elif VitesseX < 0:
                VitesseX = 0

    if position == "Downward":
        ground = -348
        if isWalking == True:
            if VitesseX > (limiteVitesse*(-1)):
                VitesseX -= acceleration

        if isWalking == False:
            if VitesseX < 0:
                VitesseX += friction
            elif VitesseX > 0:
                VitesseX = 0


    if isJumping == True:
        if inJump == False:
            VitesseY += gravite*10
            inJump = True
            onGround = False
        elif yPos > ground:
            VitesseY -= gravite
    
    if isJumping == False:
        if yPos >= ground and onGround == False:
            VitesseY -= gravite
        elif yPos < ground:
            VitesseY =0
            inJump = False
            m.sety(ground)
            onGround = True


    #Animation
    if isWalking == True:
        if MarioAnimation < 1:
            MarioAnimation = 1
            MarioCooldown = True
        elif MarioAnimation == 2 and MarioCooldown == False:
            MarioAnimation = 1
            MarioCooldown = True
        elif MarioCooldown == False:
            MarioAnimation += 1
            MarioCooldown = True

        if MarioCooldown == True:
            if MarioCooldownCounter == AnimeSpeed:
                MarioCooldown = False
                MarioCooldownCounter = 0
            else:
                MarioCooldownCounter +=1
    else:
        MarioAnimation = 0
   
   
    #updateScreenm
    m.setx(xPos+VitesseX)
    if onGround == True:
        m.sety(ground)
    else:
        m.sety(yPos+VitesseY)

    m.clear()
    MARIO(MarioScale,MarioAnimation)


    screen.update()
    screen.ontimer(GameLoop, 20)





tracer(0)                                                                               

#dessin ciel
#position de depart
home()
left(180)
justMove(650)
right(90)
justMove(550)
right(90)

#dessin
begin_fill()
color("CornFlowerBlue")
for i in range(2):
    forward(1300)
    right(90)
    forward(1000)
    right(90)
end_fill()


home()





#BUSHH AND ALLLLLLLLLLLLLLLLLLLLL

b.left(180)
bjustMove(650)
b.left(90)
bjustMove(360)
b.width(3)
b.color("Black")
b.left(90)




bush()
bjustMove(120)
bush()
bjustMove(120)
bush()
bjustMove(500)
bush()



#DESSIN SOLLLLLLLLLLLLLLLLLLLLLLLL

#position de depart
home()
up()
left(180)
forward(650)
left(90)
forward(450)
left(90)
down()


#dessin
for i in range(13):   #1er ligne
    terre()
    justMove(100)

left(180)
justMove(1300)
left(90)
justMove(100)
left(90)
for i in range(13):
    terre()
    justMove(100)
up()



#dessin bloc enAIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
home()
left(180)
justMove(200)   
left(180)
blocSpecial()
justMove(200)
brique()
justMove(100)
brique()
justMove(100)
blocSpecial()
justMove(100)
brique()




#IN GAMEEEEEEEEEEEEEEEEEEEEEEEE
m.home()
m.left(180)
mjustMove(500)
m.left(90)
mjustMove(358)
m.left(90)
MARIO(MarioScale,0)


screen.listen() 
#screen.onkey(lambda: MarioForward(10), "w")
#screen.onkey(lambda: MarioDownward(10), "s")

screen.onkeypress(Walking, "d")
screen.onkeyrelease(stopWalking, "d")
screen.onkeypress(stepBack, "a")
screen.onkeyrelease(stopWalking, "a")
screen.onkeypress(saut, "space")
screen.onkeyrelease(StopSaut, "space")

screen.listen()


#while endGame == False:
#    GameLoop()



GameLoop()
mainloop()
