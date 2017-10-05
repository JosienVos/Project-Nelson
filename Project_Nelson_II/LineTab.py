#code to draw lines with

class ClassLine(object):
    def __init__(self,xOrigin,yOrigin,inner,outer,offset,direction):
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
        self.inner = inner
        self.outer = outer
        self.offset = offset/180.0*3.14
        self.direction = direction
    
    def display(self,timer,banList):
        if self.inner > 360:
            division = 180
        elif self.inner > 180:
            division = 2
        elif self.inner > 90:
            division = 4
        elif self.inner > 45:
            division = 8
        else:
            division = 16
        if timer%division == 0:
            xInner = cos(self.direction*timer*3.14/90+self.offset)*self.inner + self.xOrigin
            xOuter = cos(self.direction*timer*3.14/90+self.offset)*self.outer + self.xOrigin
            yInner = sin(self.direction*timer*3.14/90+self.offset)*self.inner + self.yOrigin
            yOuter = sin(self.direction*timer*3.14/90+self.offset)*self.outer + self.yOrigin
            
            if banList == False or len(banList) == 0:
                for j in range(4):
                    strokeWeight(5*j+5)
                    stroke(250,150,0,255/pow(j+1,1.5))
                    line(xInner,yInner,xOuter,yOuter)
            else:
                banned = False
                for k in range(len(banList)):
                    ban = banList[k]
                    xBan = ban[0]
                    yBan = ban[1]
                    radiusBan = ban[2]
                    distance = sqrt(sq(xBan - xInner) + sq(yBan - yInner))
                    if (distance <= radiusBan):
                        banned = True
                if not banned:
                    for j in range(4):
                        strokeWeight(5*j+5)
                        stroke(250,150,0,255/pow(j+1,1.5))
                        line(xInner,yInner,xOuter,yOuter)