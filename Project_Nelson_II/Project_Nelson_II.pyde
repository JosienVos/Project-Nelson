#PROJECT NELSON 2.0
#date started: december 31st 2016
#date finished: january 6th 2017

from CircleTab import ClassCircle
from LineTab import ClassLine
from RuneTab import ClassRune

def setup():
    size(900,900)
    background(0)
    strokeWeight(5)
    stroke(0)
    
    global timer, banList
    timer = 0
    radius = 300
    offset = 270
    amountPossibilities = [3,4,5,6,7,9,11,13,17]
    totalAmount = amountPossibilities[int(random(8))]
    directionList = [-1,1]
    
    global mainCircleList, innerCircleList, smallCircleList, circleRowList, sideCircleList, tinyCircleList, extraCircleList, outerCircleList
    global circleRowBanList, sideCircleBanList, tinyCircleBanList, extraCircleBanList, outerCircleBanList
    global runeList
    
    mainCircleList = []
    direction = directionList[int(random(2))]
    mainCircleList.append(ClassCircle(width/2,height/2,radius,offset,direction))
    mainCircleList.append(ClassCircle(width/2,height/2,int(radius*1.1),offset,-direction))
    mainCircleList.append(ClassLine(width/2,height/2,int(radius*1.03),int(radius*1.07),offset,direction))
    runeList = []
    
    type = int(random(4))
    
    innerCircleList = [] #previously known as circle type A
    amount = int(random(5))
    for i in range(amount):
        if i!=0:
            smallRadius = radius - radius/i + radius/(amount+1.5)
            smallDirection = direction * pow(-1,i)
            innerCircleList.append(ClassCircle(width/2,height/2,smallRadius,offset,smallDirection))
    
    direction = directionList[int(random(2))]
    smallCircleList = [] #previously known as circle type C
    if type == 0:
        for i in range(totalAmount):
            xOrigin = width/2+cos(6.28/totalAmount*i)*radius/2
            yOrigin = height/2+sin(6.28/totalAmount*i)*radius/2
            offset = 360.0/totalAmount*i+180
            smallCircleList.append(ClassCircle(xOrigin,yOrigin,radius/2,offset,direction))
    
    circleRowList = [] #previously knnown as circle type F
    circleRowBanList = []
    if random(5) > 2 and type == 0:
        for i in range(int(random(1,3))):
            amount = totalAmount * int(random(1,3))
            bigRadius = int(radius*random(0.2,0.8))
            smallRadius = bigRadius/amount
            amount *= int(random(1,4))
            direction = directionList[int(random(2))]
            for j in range(amount):
                xOrigin = cos(j*6.28/amount) * bigRadius + width/2
                yOrigin = sin(j*6.28/amount) * bigRadius + height/2
                offset = 360.0/amount*j+180
                circleRowList.append(ClassCircle(xOrigin,yOrigin,smallRadius,offset,direction))
                circleRowBanList.append([xOrigin,yOrigin,smallRadius])
    
    sideCircleList = [] #these did not exist in Nelson v1
    tinyCircleList = []
    extraCircleList = []
    sideCircleBanList = []
    tinyCircleBanList = []
    extraCircleBanList = []
    if type == 1 or type == 3:
        amount = int(random(1,5))
        xOrigin = width/2
        yOrigin = height/2 - int(random(radius/3, radius/2+radius/5))
        maxRadius = yOrigin-height/2 + radius
        direction = directionList[int(random(2))]
        offset = 270
        for i in range(amount):
            smallRadius = maxRadius - maxRadius/(amount+3)*i
            smallDirection = direction * pow(-1,i)
            sideCircleList.append(ClassCircle(xOrigin,yOrigin,smallRadius,offset,smallDirection))
            if i == 0:
                sideCircleBanList.append([xOrigin,yOrigin,smallRadius])
        amount = int(random(4))
        for i in range(amount):
            smallRadius = 20 + 10*i
            smallDirection = direction * pow(-1,i)
            tinyCircleList.append(ClassCircle(xOrigin,yOrigin,smallRadius,offset,smallDirection))
            tinyCircleBanList.append([xOrigin,yOrigin,smallRadius])
            if i == 1 and int(random(4))==1:
                tinyCircleList.append(ClassLine(xOrigin,yOrigin,22,28,offset,direction))
        #extra circle
        yOrigin = (yOrigin*2 + maxRadius)/2
        smallRadius = maxRadius/2
        extraCircleList.append(ClassCircle(xOrigin,yOrigin,smallRadius,offset,-smallDirection))
        extraCircleBanList.append([xOrigin,yOrigin,smallRadius])
        runeList.append(ClassRune(xOrigin,yOrigin,smallRadius*0.8,int(random(20))))
    
    outerCircleList = [] #these did not exist in Nelson v1 either
    outerCircleBanList = []
    if type == 2 or type == 3:
        placesAmount = int(random(3,5))
        amount = int(random(2,4))
        midDistance = radius - int(random(radius/9,radius/7)) #hoever van het midden het staat
        maxRadius = radius - midDistance + midDistance/5
        # maxRadius = midDistance/2 + midDistance/3
        direction = directionList[int(random(2))]
        offsetMod = int(random(360/placesAmount))
        lines = int(random(2))
        for i in range(placesAmount):
            offset = 360/placesAmount * i + offsetMod
            xOrigin = width/2 + cos(offset/180.0*3.14)*midDistance
            yOrigin = height/2 + sin(offset/180.0*3.14)*midDistance
            for j in range(amount):
                smallRadius = maxRadius - maxRadius/5*j
                smallDirection = direction * pow(-1,j)
                smallRadius = maxRadius - maxRadius/(amount+3)*j
                outerCircleList.append(ClassCircle(xOrigin,yOrigin,smallRadius,offset,smallDirection))
                if j == 0:
                    outerCircleBanList.append([xOrigin,yOrigin,smallRadius])
                if j == 1 and lines==1:
                    outerCircleList.append(ClassLine(xOrigin,yOrigin,smallRadius*1.08,maxRadius*0.92,offset,direction))
                if j == amount-1 and type == 2:
                    runeList.append(ClassRune(xOrigin,yOrigin,smallRadius*0.9,int(random(20))))
    
    #outer runes :D
    if random(3) > 1:
        amount = int(random(6,24))
        smallRadius = radius/7
        for i in range(amount):
            xOrigin = cos(i*6.28/amount+1.57) * radius * 1.3 + width/2
            yOrigin = sin(i*6.28/amount+1.57) * radius * 1.3 + height/2
            runeList.append(ClassRune(xOrigin,yOrigin,smallRadius,amount+i))
    
    banList = []
    for i in range(len(sideCircleBanList)):
        banList.append(sideCircleBanList[i])
    for i in range(len(outerCircleBanList)):
        banList.append(outerCircleBanList[i])
    for i in range(len(circleRowBanList)):
        banList.append(circleRowBanList[i])

def keyPressed():
    if key == ' ':
        setup()

def draw():
    global timer, banList
    global mainCircleList, innerCircleList, smallCircleList, circleRowList, sideCircleList, tinyCircleList, extraCircleList, outerCircleList
    global circleRowBanList, sideCircleBanList, tinyCircleBanList, extraCircleBanList, outerCircleBanList
    global runeList
    
    if timer <= 180:
        for i in range(len(mainCircleList)):
            mainCircleList[i].display(timer,outerCircleBanList)
        for i in range(len(innerCircleList)):
            innerCircleList[i].display(timer,banList)
        for i in range(len(smallCircleList)):
            smallCircleList[i].display(timer,circleRowBanList)
        for i in range(len(circleRowList)):
            circleRowList[i].display(timer,False)
        for i in range(len(sideCircleList)):
            sideCircleList[i].display(timer,extraCircleBanList)
        for i in range(len(tinyCircleList)):
            tinyCircleList[i].display(timer,False)
        for i in range(len(extraCircleList)):
            extraCircleList[i].display(timer,tinyCircleBanList)
        for i in range(len(outerCircleList)):
            outerCircleList[i].display(timer,sideCircleBanList)
        for i in range(len(runeList)):
            runeList[i].display(timer)
        
        
        timer += 1