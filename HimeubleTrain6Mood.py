import turtle
import random

#palette de couleur differante qui sont ensuite pris au hasard une fois le programme lancer 
palCoul = { #ordre:coul ligneH1, coul ligneH2, coul ligneH3, coul ligneH4, coul bg,     coul1 train,  fenet train, coul3 train,  coul4 train,
    "Pal1": [     "#A75599",  "#543B6B", "#262238", "#09090E", "#ECC6FF",       "#3D2F4B", "#514683", "#917F96", "#ABA0C4"],
    "Pal2": [     "#704545",  "#5F4636", "#382F22", "#0E0D09", "#968888",       "#4B2F2F", "#835946", "#776363", "#A08885"],
    "Pal3": [     "#5564A7",  "#3B4E6B", "#222638", "#0C090E", "#C6FFFC",       "#2F2F4B", "#464A83", "#8A7F96", "#A8A0C4"],
    "Pal4": [     "#76A755",  "#3B6B5F", "#223838", "#090B0E", "#E0FFC6",       "#2F384B", "#465983", "#827F96", "#A0ABC4"],
    "Pal5": [     "#A1A1A1",  "#6E6E6E", "#2B2B2B", "#000000", "#FF0000",       "#141414", "#6D0000", "#C7C7C7", "#FFFFFF"],
    "Pal6": [     "#10160C",  "#203D18", "#28961A", "#2BFF00", "#000000",       "#0A1805", "#56FF34", "#000000", "#000000"],
    "Pal7": [     "#160C16",  "#3C183D", "#961A8C", "#FF00EA", "#000000",       "#180518", "#EE34FF", "#000000", "#000000"],
    } 

randomColor= random.randint(1,6)
#randomColor = int(input("choisisez un nombre entre 1 et 7 pour les differente couleurs du dessin!\n>  "))   #je prefere quand c'est directement aleatoir, mais vous pouvez activer cet ligne pour choisir manuelement la couleur au debut du programme :)
print(randomColor)
modeEpileptic = False

turtle.bgcolor(palCoul[f"Pal{randomColor}"][4])
v = turtle.Turtle()
r = turtle.Turtle()
v.hideturtle()
r.hideturtle()
s = turtle.Screen()
turtle.tracer(0)
taille = 30  #taille des pixel du train

ligne1 = [] #liste pour contenir la largeur/hauteur des himeuble par ligne  (ligne 1 est la ligne la plus lointaine) ces liste sont ramplis dans la fonction ligneHiumeuble
ligne2 = []
ligne3 = []
ligne4 = []

def rectangle(longr, hautr):
    r.begin_fill()
    for i in range(2):
        r.forward(longr)
        r.left(90)
        r.forward(hautr)
        r.left(90)
    r.end_fill()

def TP(stylo, posiX, posiY):
    stylo.up()
    stylo.goto(posiX, posiY)
    stylo.down()

def himeuble(long, etage, couleur):
    #base de création d'un himeuble, je compte en etage (1 etage vaut 20 pixel)
    v.color(couleur)
    v.begin_fill()
    for i in range(2):
        v.forward(long)
        v.left(90)
        v.forward(10)
        for i in range(etage):
            v.forward(20)
        v.left(90)
    v.end_fill()
     
def ligneHiumeuble(coul1,minEtage=10,maxEtage=50,ligne=0):
    #ca crée une ligne de 20 himeuble de maniere random et les stock dans une liste differante pour chaque ligne d'himeuble (ligne1,ligne2 ect..)
    TP(v, -1500,-700)
    for i in range(20):
        LONG = random.randint(100,300)
        ETAGE = random.randint(minEtage,maxEtage)
        basePos = v.pos()
        himeuble(LONG, ETAGE, coul1)
        v.up()
        v.goto(basePos[0],basePos[1])
        v.forward(LONG)
        v.down()

        if ligne==1: 
            ligne1.append(f"{LONG}/{ETAGE}")
        elif ligne==2:
            ligne2.append(f"{LONG}/{ETAGE}")
        elif ligne==3:
            ligne3.append(f"{LONG}/{ETAGE}")
        elif ligne==4:
            ligne4.append(f"{LONG}/{ETAGE}")
        
def afficherHimeuble(ligne,ligneType):
    #affiche les himeuble contenu dans les liste
    posi = v.pos()
    if ligneType==1: 
        couleure = palCoul[f"Pal{randomColor}"][0]
    elif ligneType==2:
        couleure =palCoul[f"Pal{randomColor}"][1]
    elif ligneType==3:
        couleure =palCoul[f"Pal{randomColor}"][2]
    elif ligneType ==4:
        couleure =palCoul[f"Pal{randomColor}"][3]

    for i in range(20):
        long_etage = ligne[i]
        long_etage = long_etage.split("/")
        long = long_etage[0]
        etage = long_etage[1]

        himeuble(int(long),int(etage),couleure)
        v.up()
        v.forward(int(long))
        v.down()
    v.up()
    v.goto(posi[0],posi[1])
    v.down()

def noir():
    #crée des bordure noir que j'utiliserais en haut et en bas pour un effet tunnel
    r.color("black")
    rectangle(3000,500)

def barriere():#crée la barre de la barriere (bouge pas)
    r.color("black")
    rectangle(3000,30)
def LignebarBarriere(): #crée les barreau (bougent)
    for i in range(52):
        rectangle(25,70)
        r.up()
        r.forward(60)
        r.down


def onlyMove(step):
    r.up()
    r.forward(step)
    r.down()


def pixel(couleur):  #pixel pour le train
    r.color(couleur)
    r.begin_fill()
    for i in range(4):
        r.forward(taille)
        r.left(90)
    r.end_fill()
    onlyMove(taille)

def lignePixel(couleur, long): # ligne de pixel (pour alleger un peu le programme, dessiner pixel par pixel etait trop lourd)
    r.color(couleur)
    r.begin_fill()

    r.forward(taille*long)
    posBase = r.pos()
    r.left(90)
    r.forward(taille)
    r.left(90)
    
    r.forward(taille*long)
    r.left(90)
    r.forward(taille)
    r.left(90)

    TP(r,posBase[0], posBase[1])
    r.end_fill()


def wagon(coul1,coul2, coul3,coul4):
    basePos = r.pos()
    lignePixel(coul1, 22)

    TP(r,basePos[0], basePos[1]+taille)
    lignePixel(coul4, 22)
    TP(r,basePos[0], basePos[1]+taille*2)
    lignePixel(coul4, 22)

    TP(r,basePos[0], basePos[1]+taille*3)
    lignePixel(coul3, 4)
    lignePixel(coul2, 4)
    for i in range(2):
        lignePixel(coul3, 2)
        lignePixel(coul2, 4)
    lignePixel(coul3, 2)

    for i in range(2):
        TP(r,basePos[0], basePos[1]+taille*(i+4))
        lignePixel(coul4, 4)
        lignePixel(coul2, 4)
        for i in range(2):
            lignePixel(coul4, 2)
            lignePixel(coul2, 4)
        lignePixel(coul4, 2)

    TP(r,basePos[0], basePos[1]+taille*6)
    lignePixel(coul4, 22)

    TP(r,basePos[0], basePos[1])

def train(nmbWagon, coul1,coul2,coul3,coul4):
    for i in range (nmbWagon):
        wagon(coul1, coul2, coul3, coul4)
        onlyMove(taille*24)
    
    wagon(coul1, coul2, coul3, coul4)
    onlyMove(taille*22)

    basePos = r.pos()
    lignePixel(coul1,8)
    TP(r,basePos[0],basePos[1]+taille)
    lignePixel(coul4,5)
    lignePixel(coul1,3)

    TP(r,basePos[0],basePos[1]+taille*2)
    lignePixel(coul4,5)
    lignePixel(coul1,3)

    TP(r,basePos[0],basePos[1]+taille*3)
    lignePixel(coul3,4)
    lignePixel(coul2,3)

    TP(r,basePos[0],basePos[1]+taille*4)
    lignePixel(coul4,3)
    lignePixel(coul2,3)

    TP(r,basePos[0],basePos[1]+taille*5)
    lignePixel(coul4,3)
    lignePixel(coul2,2)

    TP(r,basePos[0],basePos[1]+taille*5)
    lignePixel(coul4,2)
    lignePixel(coul2,2)

    TP(r,basePos[0],basePos[1]+taille*6)
    lignePixel(coul1,3)


#creation scene
ligneHiumeuble(palCoul[f"Pal{randomColor}"][0],20,50,1)
ligneHiumeuble(palCoul[f"Pal{randomColor}"][1],10,40,2)
ligneHiumeuble(palCoul[f"Pal{randomColor}"][2],5,30,3)
ligneHiumeuble(palCoul[f"Pal{randomColor}"][3],5,20,4)

TP(v, 1500,-500)
barriere()

TP(v,-1500,-500)
basePos = v.pos()
Xpos1 = basePos[0]
Xpos2 = basePos[0]
Xpos3 = basePos[0]
Xpos4 = basePos[0]
XposBar = 1250
n=0
n1=0
n2=0
n3=0
n4=0

def gameLoop():#se repete toute les 20 mls
    global Xpos1,Xpos2,Xpos3,Xpos4,XposBar, n,n1,n2,n3,n4     ,randomColor
    n +=1
    n1+=1#variables pour le nombre de fois la fonction gameLoop a ete appeler, n ne se reinisalise pas, n1 est pour la ligne1 (il se reistialise quand ligne1 est partit trop loin), 2 pour ligne2.. ect..
    n2+=1
    n3+=1
    n4+=1
    v.clear()
    if n1 >= int(ligne1[0].split("/")[0]) : #supprime un ou plusieur himeuble selon la ligne et en reconstruit un ou plusieur apres de maniere random pour pouvoir faire defiler les himeuble de maniere infini >w<
        n1=0
        Xpos1 += int(ligne1[0].split("/")[0]) 
        ligne1.pop(0)
        ligne1.append(f"{random.randint(100,300)}/{random.randint(20,50)}")

    if n2 >=int(ligne2[0].split("/")[0]) :
        n2=0
        for i in range(2):
            Xpos2 += int(ligne2[0].split("/")[0])
            ligne2.pop(0)
            ligne2.append(f"{random.randint(100,300)}/{random.randint(10,40)}")

    if n3 >=int(ligne3[0].split("/")[0]) :
        n3=0
        for i in range(3):
            Xpos3 += int(ligne3[0].split("/")[0])
            ligne3.pop(0)
            ligne3.append(f"{random.randint(100,300)}/{random.randint(5,30)}")
        
    if n4 >=int(ligne4[0].split("/")[0]) :
        n4=0
        for i in range(4):
            Xpos4 += int(ligne4[0].split("/")[0])
            ligne4.pop(0)
            ligne4.append(f"{random.randint(100,300)}/{random.randint(5,20)}")

    #affiche les himeuble
    Xpos1 -=1
    TP(v, Xpos1,basePos[1])
    afficherHimeuble(ligne1,1)

    Xpos2 -=2
    TP(v, Xpos2,basePos[1])
    afficherHimeuble(ligne2,2)

    Xpos3 -=3
    TP(v, Xpos3,basePos[1])
    afficherHimeuble(ligne3,3)

    Xpos4 -=4
    TP(v, Xpos4,basePos[1])
    afficherHimeuble(ligne4,4)
    
    r.setheading(180)
    TP(r, 1300,1000)
    r.clear()
    noir()
    
    TP(r, 1300, -200)
    barriere()
    if n % 2 ==0:  #verifie si n est multiple de 2 et bouge en fonction du resultat pour avoir un effet de mouvement
        XposBar -=100
    else:
        XposBar = 1250
    TP(r, XposBar, -230)
    LignebarBarriere()

    TP(r, 1300, -300)
    noir()

    TP(r,-1900,-350)
    r.setheading(0)

    train(2,palCoul[f"Pal{randomColor}"][5],palCoul[f"Pal{randomColor}"][6], palCoul[f"Pal{randomColor}"][7], palCoul[f"Pal{randomColor}"][8])
    turtle.update()
    s.ontimer(gameLoop, 20)

    if modeEpileptic == True:
        if randomColor < 6:
            randomColor +=1
        else:
            randomColor = 1

gameLoop()
turtle.mainloop()