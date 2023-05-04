from graphics import *

bg = GraphWin('Splish Splash Background Design', 800,480)
bg.setBackground('royalblue4')
bg.setCoords(0, 0, 800, 480)


def draw_rectangle(x1,y1,x2,y2,color,out):
    pt1 = Point(x1,y1)
    pt2 = Point(x2,y2)
    aRectangle = Rectangle(pt1, pt2)
    aRectangle.setFill(color)
    aRectangle.setOutline(out)
    aRectangle.draw(bg)


def draw_polygon(coorX1, coorY1, coorX2, coorY2, coorX3, coorY3, coorX4, coorY4, color, out):
    pt1 = Point(coorX1, coorY1)
    pt2 = Point(coorX2, coorY2)
    pt3 = Point(coorX3, coorY3)
    pt4 = Point(coorX4, coorY4)
    aPoly = Polygon(pt1,pt2,pt3,pt4)
    aPoly.setFill(color)
    aPoly.setOutline(out)
    aPoly.draw(bg)

design = Image(Point(400,260), "design.png")
design.draw(bg)

draw_rectangle(0,0,800,20, 'deepskyblue4', 'deepskyblue4')
draw_polygon(40,250,100,200,120,0,0,0,'skyblue4','skyblue4')
draw_polygon(50,240,120,200,140,0,0,0,'deepskyblue4','deepskyblue4')

draw_polygon(180,190,270,220,310,0,150,0,'skyblue4','skyblue4')
draw_polygon(180,180,250,200,290,0,150,0,'deepskyblue4','deepskyblue4')

draw_polygon(380,260,450,250,460,0,290,0,'skyblue4','skyblue4')
draw_polygon(370,210,430,200,460,0,290,0,'deepskyblue4','deepskyblue4')

draw_polygon(480,160,540,160,500,0,480,0,'skyblue4','skyblue4')
draw_polygon(480,150,530,150,490,0,460,0,'deepskyblue4','deepskyblue4')

draw_polygon(550,190,600,190,650,0,540,0,'skyblue4','skyblue4')
draw_polygon(570,170,600,170,650,0,550,0,'deepskyblue4','deepskyblue4')

draw_polygon(760,230,680,160,650,0,800,0,'skyblue4','skyblue4')
draw_polygon(760,230,690,160,650,0,800,0, 'deepskyblue4','deepskyblue4')
draw_rectangle(0,30,800,0, 'deepskyblue4', 'deepskyblue4')


bg.getMouse()
