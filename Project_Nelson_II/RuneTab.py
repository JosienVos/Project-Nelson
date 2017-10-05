#code to draw runes with

def drawPoint(x,y): #glow
    for i in range(4):
        strokeWeight(5*i+5)
        stroke(250,150,0,255/pow(i+1,3))
        point(x,y)

def runeZero(xOrigin,yOrigin,radius,timer): #een gespiegelde heel kromme r ongeveer
    if timer < 10:
        x = xOrigin - radius/2 + cos(timer/45.0*3.14+3.14)*radius+radius-radius/5
        y = yOrigin - sin(-timer/90.0*3.14)*radius - radius
    elif timer < 40:
        x = xOrigin - radius/2
        y = yOrigin - sin(-timer/90.0*3.14)*radius - radius
    elif timer < 140:
        x = timer*radius/100.0+xOrigin-radius*0.9
        y = sin(timer/90.0*3.14)*radius/2+yOrigin-radius/2
    else:
        x = xOrigin + radius/2
        y = yOrigin + sin(timer/90.0*3.14)*radius
    drawPoint(x,y+radius/2)

def runeOne(xOrigin,yOrigin,radius,timer): #omgekeerde N met een boogje aan het begin
    if timer < 90:
        x = timer*radius/90.0+xOrigin-radius/2
        y = sin(timer/45.0*3.14)*radius/5+yOrigin-radius
    elif timer < 130:
        x = -cos((timer+45)/90.0*3.14)*radius/3+xOrigin+radius/2
        y = timer*radius/90.0+yOrigin-radius*2
    else:
        x = xOrigin-radius/3+radius/2
        y = timer*radius/90.0+yOrigin-radius*2
    drawPoint(x,y+radius/2)

def runeTwo(xOrigin,yOrigin,radius,timer): #spiraal
    distance = radius*0.7 - timer/180.0*radius*0.7
    x = cos(timer/45.0*3.14)*(distance)+xOrigin
    y = sin(timer/45.0*3.14)*(distance)+yOrigin
    drawPoint(x,y)

def runeThree(xOrigin,yOrigin,radius,timer): #oog (mislukte spiraal maar who cares)
    distance = radius/2 - timer/180.0*radius
    x = cos(timer/45.0*3.14)*(distance)+xOrigin
    y = -sin(timer/45.0*3.14)*(distance)+yOrigin
    drawPoint(x,y)

def runeFour(xOrigin,yOrigin,radius,timer): #vierkantje
    if timer < 45:
        x = xOrigin - radius/2 + cos(timer/90.0*3.14)*radius
        y = yOrigin + radius/2
    elif timer < 90:
        x = xOrigin - radius/2
        y = yOrigin - radius/2 + sin(timer/90.0*3.14)*radius
    elif timer < 135:
        x = xOrigin + radius/2 + cos(timer/90.0*3.14)*radius
        y = yOrigin - radius/2
    else:
        x = xOrigin + radius/2
        y = yOrigin + radius/2 - sin(-timer/90.0*3.14)*radius
    drawPoint(x,y)

def runeFive(xOrigin,yOrigin,radius,timer): #lissajous
    x = xOrigin + cos(timer/14.25*3.14/2)*radius/2
    y = yOrigin + sin(timer/14.25*3.14/3)*radius/2
    drawPoint(x,y)

def runeSix(xOrigin,yOrigin,radius,timer): #oneindigheid
    x = xOrigin + cos(timer/45.0*3.14/2)*radius/2
    y = yOrigin + sin(timer/45.0*3.14)*radius/2
    drawPoint(x,y)

def runeSeven(xOrigin,yOrigin,radius,timer): #plectrum
    x = xOrigin + cos(timer/90.0*3.14+1.57) * radius/2
    y = yOrigin + sin(timer/90.0*3.14/2) * radius - radius/2
    drawPoint(x,y)

def runeEight(xOrigin,yOrigin,radius,timer): #twee gekruiste ovalen
    x = xOrigin - cos(1.57+timer/90.0*3.14) * radius/2
    y = yOrigin - sin(1.57+timer/90.0*3.14+1.57/2) * radius/2
    drawPoint(x,y)
    x = xOrigin + cos(1.57+timer/90.0*3.14) * radius/2
    y = yOrigin + sin(1.57+timer/90.0*3.14-1.57/2) * radius/2
    drawPoint(x,y)

def runeNine(xOrigin,yOrigin,radius,timer): #hartje (deze is lame!)
    x = xOrigin + cos(1.57+timer/180.0*3.14) * radius/2
    y = yOrigin + sin(1.57+timer/180.0*3.14+1.57/2) * radius/2
    drawPoint(x,y)
    x = xOrigin - cos(1.57+timer/180.0*3.14) * radius/2
    y = yOrigin - sin(1.57+timer/180.0*3.14-1.57/2) * radius/2
    drawPoint(x,y)

class ClassRune(object):
    def __init__(self,xOrigin,yOrigin,radius,type):
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
        self.radius = radius
        self.type = type%10
    
    def display(self,timer):
        if self.type == 0:
            runeZero(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 1:
            runeOne(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 2:
            runeTwo(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 3:
            runeThree(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 4:
            runeFour(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 5:
            runeFive(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 6:
            runeSix(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 7:
            runeSeven(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 8:
            runeEight(self.xOrigin,self.yOrigin,self.radius,timer)
        if self.type == 9:
            runeNine(self.xOrigin,self.yOrigin,self.radius,timer)