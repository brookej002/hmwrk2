
from graphics import*
win= GraphWin('Faces', 200, 150)
win.yUp()

def makeFace(center, win):
    head=Circle(center, 25)
    head.setFill("purple")
    head.draw(win)

    eye1Center = center.clone()
    eye1Center.move(-10,5)
    eye1 =  Circle(eye1Center, 5)
    eye1.setFill("blue")
    eye1.draw(win)

    eye2End1=eye1Center.clone()
    eye2End1.move(15,0)
    eye2End2= eye2End1.clone()
    eye2End2.move(10, 0)

    eye2= Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    noseSide1= center.clone()
    nose1.move(-8,8)
    NoseSide2= center.clone()
    nose2.move(-6,6)
    NoseSide3= center.clone()
    nose3.move(0,0)
    Vertices= [noseSide1, noseSide2, noseSide3]

    nose= Polygon(vertices)
    nose.setFill('pink')
    nose.draw(win)

    mouthCorner1= center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2=mouthCorner1.clone()
    mouthCorner2.move(20,-5)

    mouth=Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("black")
    mouth.draw(win)

    return [head, eye1, eye2, nose, mouth]

def main():
    for i in range(6):
        win.getMouse()
        head = Circle(Point(40,100), 25)
        head.setFill("yellow")
        head.draw(win)
        eye1 = Circle(Point(30, 105), 5)
        eye1.setFill('blue')
        eye1.draw(win)
        eye2 = Line(Point(45, 105), Point(55, 105))
        eye2.setWidth(3)
        eye2.draw(win)
        mouth = Oval(Point(30, 90), Point(50, 85))
        mouth.setFill("red")
        mouth.draw(win)
