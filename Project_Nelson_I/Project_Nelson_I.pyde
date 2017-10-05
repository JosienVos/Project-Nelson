# dit is een programma dat random sigils kan genereren
# laatste keer dat ik het berekende waren er ruim 2 miljard verschillende sigils mogelijk
# gemaakt door Josien Vos, oktober-november 2016

def setup():
    size(800,800)
    background(0)
    strokeWeight(3)
    START()

def keyPressed():
    START()
    
def START():
    global done, radius, circleAtype, circleAamount, circleBamount
    global circleCamount, circleDamount, circleDtype, circleEamount, circleFamount
    global polygonAsides, polygonBamount, polygonBsides, polygonBtype, polygonCsides
    global polygonDamount, polygonDsize, triangleAamount, triangleAcolour
    global stripesAamount, stripesAstart, stripesAend, dotsAamount, dotsArows, dotsAtype
    global colour, backgroundColour
    
    amountPossibilities = [3,4,5,6,7,9,11,13,17]
    circleDpossibilities = (0,1,2,4)
    done = False
    
    colour = (200,0,0)
    backgroundColour = (250,250,250)
    
    #hierna komen de randomizers voor de hoeveelheid cirkels enzo
    #alles wat je aan wil passen moet je hier doen
    radius = 300
    totalAmount = amountPossibilities[int(random(8))]
    
    circleAtype = int(random(0,3))
    circleAamount = int(random(6))
    circleBamount = totalAmount
    circleCamount = totalAmount * int(random(3))
    circleDamount = totalAmount * circleDpossibilities[int(random(0,2))]
    circleDtype = int(random(0,4))
    circleEamount = totalAmount * int(random(3))
    circleFamount = totalAmount * int(random(1,3))
    
    polygonAsides = totalAmount * int(random(2))
    polygonBamount = int(random(6))
    polygonBsides = totalAmount * int(random(2))
    polygonBtype = int(random(3))
    polygonCsides = totalAmount
    polygonDamount = totalAmount
    polygonDsize = random(5)
    triangleAamount = totalAmount * int(random(1,3))
    triangleAcolour = int(random(1,3))
    
    stripesAamount = totalAmount * circleDpossibilities[int(random(2))]
    stripesAstart = random(1.05,5)
    stripesAend = stripesAstart + random(0.1,0.3)
    dotsAamount = totalAmount * int(random(3))
    dotsArows = int(random(5))
    dotsAtype = int(random(3))
    
    while circleCamount > 10 and circleCamount%2 == 0:
        circleCamount = circleCamount/2
    while circleDamount > 10 and circleDamount%2 == 0:
        circleDamount = circleDamount/2
    if circleEamount > 20 and circleEamount%2 == 0:
        circleEamount = circleEamount/2
    
    if circleCamount == circleDamount and circleDtype != 0:
        circleCamount = 0
    
    if polygonAsides > 8 and polygonAsides%2 == 0:
        polygonAsides = int(polygonAsides/2)
    while polygonCsides < 10:
        polygonCsides = polygonCsides*2
    
    
    background(backgroundColour[0],backgroundColour[1],backgroundColour[2])


#hier zullen de verschillende manieren van tekenen worden gedefinieerd


def drawPoint(x,y): #bepaalt of een stip wel of niet gezet moet worden
    global colour, backgroundColour
    strokeWeight(3)
    if not (x-width/2)**2 + (y-height/2)**2 >= radius**2 + 60:
        strokeWeight(3)
        stroke(colour[0],colour[1],colour[2])
        point(x,y)
        
def drawLine(xA,yA,xB,yB): #tekent een lijn in de goede kleur met de goede dikte
    global colour, backgroundColour
    strokeWeight(3)
    stroke(colour[0],colour[1],colour[2])
    line(xA,yA,xB,yB)


#vanaf hier worden de verschillende types cirkels gedefinieerd


def circleMain(radius): #de grote cirkel waarbinnen de rest zit
    global colour
    strokeWeight(3)
    for i in range(720):
        x = cos(i) * radius
        y = sin(i) * radius
        stroke(colour[0],colour[1],colour[2])
        point(x+width/2,y+height/2)

def circleTypeA(radius,amount,type): #binnencirkels van hoofdcirkel
    for i in range(1,amount+1):
        if type == 0:
            howBig = radius*i/amount
        elif type == 1:
            howBig = radius/i - radius/(amount+1.5)
        else:
            howBig = radius - radius/i + radius/(amount+1.5)
        
        for j in range(720):
            x = cos(j) * howBig
            y = sin(j) * howBig
            drawPoint(x+width/2,y+height/2)

def circleTypeB(radius,amount): #grote cirkels die ook buiten hoofdcirkel verdergaan
    for i in range(amount):
        xOrigin = cos(i*6.28/amount) * radius * 1.2 + width/2
        yOrigin = sin(i*6.28/amount) * radius * 1.2 + height/2
        for j in range(720):
            x = cos(j) * radius * 1.2
            y = sin(j) * radius * 1.2
            drawPoint(x+xOrigin,y+yOrigin)

def circleTypeC(radius,amount): #kleine cirkels half formaat van hoofd, zitten erbinnen
    for i in range(amount):
        xOrigin = cos(i*6.28/amount) * radius * .5 + width/2
        yOrigin = sin(i*6.28/amount) * radius * .5 + height/2
        for j in range(360):
            x = cos(j) * radius * .5
            y = sin(j) * radius * .5
            drawPoint(x+xOrigin,y+yOrigin)

def circleTypeD(radius,amount): #de kringeltjes cirkels
    global circleDtype
    if circleDtype == 1 or circleDtype == 2:
        for i in range(360*4):
            x = cos(i/6.28+3.14)*radius*0.7 + cos(i/6.28*(amount+1)+3.14)*50
            y = sin(i/6.28+3.14)*radius*0.7 + sin(i/6.28*(amount+1)+3.14)*50
            drawPoint(x+width/2,y+height/2)
    if circleDtype == 2 or circleDtype == 3:
        for i in range(360*4):
            x = cos(i/6.28)*radius*0.4 + cos(i/6.28*(amount+1))*50
            y = sin(i/6.28)*radius*0.4 + sin(i/6.28*(amount+1))*50
            drawPoint(x+width/2,y+height/2)

def circleTypeE(radius,amount): #cirkels die er half buiten vallen
    for i in range(amount):
        xOrigin = cos(i*6.28/amount) * radius + width/2
        yOrigin = sin(i*6.28/amount) * radius + height/2
        for j in range(360):
            x = cos(j) * radius * .5
            y = sin(j) * radius * .5
            drawPoint(x+xOrigin,y+yOrigin)

def circleTypeF(radius,amount): #kleinere cirkels die samen in een kringetje staan
    for i in range(int(random(1,4))):
        smallRadius = radius*random(0.2,0.8)
        amountF = amount * int(random(1,3))
        for j in range(amountF):
            xOrigin = cos(j*6.28/amountF) * smallRadius + width/2
            yOrigin = sin(j*6.28/amountF) * smallRadius + height/2
            for k in range(360):
                x = cos(k) * smallRadius/amountF*3
                y = sin(k) * smallRadius/amountF*3
                drawPoint(x+xOrigin,y+yOrigin)



#VANAF HIER VEELHOEKEN



def polygonTypeA(radius,sides): #een pentagram of met andere hoeveelheden hoekpunten
    if sides > 0:
        for i in range(sides*2+1):
            x = cos((i*3.14+(i%2*3.14*sides))/sides)*radius+width/2
            y = sin((i*3.14+(i%2*3.14*sides))/sides)*radius+height/2
            if i > 0:
                drawLine(x,y,xOld,yOld)
            xOld = x
            yOld = y

def polygonTypeB(radius,sides,amount,type): #veelhoeken zoals cirkel type A
    if sides > 0:
        for i in range(1,amount+1):
            if type == 0:
                howBig = radius*i/amount
            elif type == 1:
                howBig = radius/i - radius/(amount+1.5)
            else:
                howBig = radius - radius/i + radius/(amount+1.5)
        
            for j in range(sides+1):
                x = cos(j*6.28/sides) * howBig + width/2
                y = sin(j*6.28/sides) * howBig + height/2
                if j > 0:
                    drawLine(x,y,xOld,yOld)
                xOld = x
                yOld = y

def polygonTypeC(radius,sides): #tussen de twee maincircles
    if sides > 0:
        radius = radius+20
        for i in range(sides+1):
            x = cos(i*6.28/sides) * radius + width/2
            y = sin(i*6.28/sides) * radius + height/2
            if i > 0:
                drawLine(x,y,xOld,yOld)
            xOld = x
            yOld = y

def polygonTypeD(radius,amount,Dsize): #puntjes die naar binnen wijzen
    if amount > 1:
        for i in range(amount):
            xFirst = cos(i*6.28/amount+3.14/amount) * radius + width/2
            yFirst = sin(i*6.28/amount+3.14/amount) * radius + height/2
            x = cos(i*6.28/amount) * radius*Dsize/6 + width/2
            y = sin(i*6.28/amount) * radius*Dsize/6 + height/2
            xLast = cos(i*6.28/amount-3.14/amount) * radius + width/2
            yLast = sin(i*6.28/amount-3.14/amount) * radius + height/2
            drawLine(xFirst,yFirst,x,y)
            drawLine(x,y,xLast,yLast)



#VANAF HIER NOG WAT RANDOM ANDERE MEUK



def dotsTypeA(radius,amount,row,type): #want stipjes zijn lief
    for i in range(1,row):
        if type == 0:
            howBig = radius*i/row
        elif type == 1:
            howBig = radius/i - radius/(row+1.5)
        else:
            howBig = radius - radius/i + radius/(row+1.5)
        
        for j in range(amount):
            x = cos(j*6.28/amount+3.14) * howBig
            y = sin(j*6.28/amount+3.14) * howBig
            strokeWeight(6)
            point(x+width/2,y+height/2)

def stripesTypeA(radius,amount,stripeStart,stripeEnd):
    global colour, backgroundColour
    for something in range(int(random(3,4))):
        for i in range(amount):
            x = cos(i*6.28/amount)
            y = sin(i*6.28/amount)
            drawLine(x*radius/stripeStart+width/2,y*radius/stripeStart+height/2,x*radius/stripeEnd+width/2,y*radius/stripeEnd+height/2)
            stroke(backgroundColour[0],backgroundColour[1],backgroundColour[2])
            strokeWeight(5)
            point(x*radius/stripeStart+width/2,y*radius/stripeStart+height/2)
            point(x*radius/stripeEnd+width/2,y*radius/stripeEnd+height/2)
        stripeStart = random(1.05,5)
        stripeEnd = stripesAstart + random(0.1,0.3)

def triangleTypeA(radius,amount,colourType):
    global colour, backgroundColour
    if colourType == 0:
        fill(0,0,0,0)
    elif colourType == 1:
        fill(colour[0],colour[1],colour[2])
    else:
        fill(backgroundColour[0],backgroundColour[1],backgroundColour[2])
    stroke(colour[0],colour[1],colour[2])
    
    if amount < 10:
        siz = .5
    else:
        siz = 1
    
    triangleType = int(random(3))
    howBigA = int(random(2,9))/10.0
    howBigB = int(random(2,9))/10.0
    if howBigA-0.1 == howBigB:
        howBigA += 0.2
    
    if triangleType > 0:
        for i in range (amount):
            firstpointX = cos(i*6.28/amount) * howBigA * radius + width/2
            firstpointY = sin(i*6.28/amount) * howBigA * radius + height/2
            secondpointX = cos(i*6.28/amount+3.14/amount*siz) * (howBigA-0.1) * radius + width/2
            secondpointY = sin(i*6.28/amount+3.14/amount*siz) * (howBigA-0.1) * radius + height/2
            thirdpointX = cos(i*6.28/amount-3.14/amount*siz) * (howBigA-0.1) * radius + width/2
            thirdpointY = sin(i*6.28/amount-3.14/amount*siz) * (howBigA-0.1) * radius + height/2
            triangle(firstpointX,firstpointY,secondpointX,secondpointY,thirdpointX,thirdpointY)
    if triangleType < 10:
        for i in range (amount):
            firstpointX = cos(i*6.28/amount) * howBigB * radius + width/2
            firstpointY = sin(i*6.28/amount) * howBigB * radius + height/2
            secondpointX = cos(i*6.28/amount+3.14/amount*siz) * radius * (howBigB+0.1) + width/2
            secondpointY = sin(i*6.28/amount+3.14/amount*siz) * radius * (howBigB+0.1) + height/2
            thirdpointX = cos(i*6.28/amount-3.14/amount*siz) * radius * (howBigB+0.1) + width/2
            thirdpointY = sin(i*6.28/amount-3.14/amount*siz) * radius * (howBigB+0.1) + height/2
            triangle(firstpointX,firstpointY,secondpointX,secondpointY,thirdpointX,thirdpointY)


#DE DRAW FUNCTIE. DAAR IS HIJ DAN EINDELIJK.


def draw():
    global done, radius, circleAtype, circleAamount, circleBamount
    global circleCamount, circleDamount, circleDtype, circleEamount, circleFamount
    global polygonAsides, polygonBamount, polygonBsides, polygonBtype, polygonCsides
    global polygonDamount, polygonDsize, triangleAamount, triangleAcolour
    global stripesAamount, stripesAstart, stripesAend, dotsAamount, dotsArows, dotsAtype
    global colour, backgroundColour
    
    if not done:
        stripesTypeA(radius,stripesAamount,stripesAstart,stripesAend)
        
        circleTypeA(radius,circleAamount,circleAtype)
        circleTypeB(radius,circleBamount)
        circleTypeC(radius,circleCamount)
        circleTypeD(radius,circleDamount)
        circleTypeE(radius,circleEamount)
        circleTypeF(radius,circleFamount)
        
        polygonTypeA(radius,polygonAsides)
        polygonTypeB(radius,polygonBsides,polygonBamount,polygonBtype)
        polygonTypeC(radius,polygonCsides)
        polygonTypeD(radius,polygonDamount,polygonDsize)
        triangleTypeA(radius,triangleAamount,triangleAcolour)
        
        dotsTypeA(radius,dotsAamount,dotsArows,dotsAtype)
        
        circleMain(radius)
        circleMain(radius+20)
        
        fill(colour[0],colour[1],colour[2])
        
        #who really cares about the text anyway
        #text('Radius: '+str(radius),15,15)
        #text('A type: '+str(circleAtype),15,30)
        #text('A: '+str(circleAamount),15,45)
        #text('B: '+str(circleBamount),15,60)
        #text('C: '+str(circleCamount),15,75)
        #text('D: '+str(circleDamount),15,90)
        #text('D type: '+str(circleDtype),15,105)
        #text('E: '+str(circleEamount),15,120)
        #text('Poly: '+str(polygonAsides),15,135)
        #text('Poly B: '+str(polygonBamount),15,150)
        #text('Poly B type: '+str(polygonBtype),15,165)
        #text('Stripes: '+str(stripesAamount),15,180)
        
        done = True