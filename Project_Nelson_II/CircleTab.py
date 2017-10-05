#code to draw circles with
def drawCircle(radius,xOrigin,yOrigin,offset,direction,timer,banList):
    colour = [250,150,0]
    x = cos((direction*timer)/90.0*3.14+offset) * radius + xOrigin
    y = sin((direction*timer)/90.0*3.14+offset) * radius + yOrigin
    smoothener = 50.0/radius
    iRange = int(radius/50+1)
    if timer == 180:
        iRange = 1
    for i in range(iRange):
        x = cos((direction*timer+smoothener*i)/90.0*3.14+offset) * radius + xOrigin
        y = sin((direction*timer+smoothener*i)/90.0*3.14+offset) * radius + yOrigin
        
        if banList == False or len(banList) == 0:
            for j in range(4):
                strokeWeight(5*j+5)
                stroke(colour[0],colour[1],colour[2],255/pow(j+1,3))
                point(x,y)
        else:
            banned = False
            for k in range(len(banList)):
                ban = banList[k]
                xBan = ban[0]
                yBan = ban[1]
                radiusBan = ban[2]
                # fill(250,0,0)
                # ellipse(xBan,yBan,radiusBan-5,radiusBan-5)
                distance = sqrt(sq(xBan - x) + sq(yBan - y))
                if (distance <= radiusBan):
                    banned = True
            if not banned:
                for j in range(4):
                    strokeWeight(5*j+5)
                    stroke(colour[0],colour[1],colour[2],255/pow(j+1,3))
                    point(x,y)
        



class ClassCircle(object):
    def __init__(self,xOrigin,yOrigin,radius,offset,direction):
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
        self.radius = radius
        self.offset = offset/180.0*3.14
        self.direction = direction
    
    def display(self,timer,banList):
        drawCircle(self.radius,self.xOrigin,self.yOrigin,self.offset,self.direction,timer,banList)


# class ClassMainCircle(object):
#     def __init__(self,xOrigin,yOrigin,radius,offset):
#         self.xOrigin = xOrigin
#         self.yOrigin = yOrigin
#         self.radius = radius
#         self.offset = offset/180.0*3.14
    
#     def display(self,timer):
#         drawCircle(self.radius,self.xOrigin,self.yOrigin,self.offset,timer)