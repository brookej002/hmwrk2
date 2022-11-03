'''changeScene.py (2.4.5.2)'''

from graphics import* 

def main ():
    win= GraphWin('changeScene', 200, 150)
    win.yUp()
    head= Circle(Point (40,100), 25)
    head.setFill('purple')
    head.draw(win)
    eye1=Line(Point(30, 105), Point (40,105))
    eye1.setWidth(3)
    eye1.draw(win)
    eye2=Line(Point(45,105), Point (55, 105))
    eye2.setWidth(3)
    eye2.draw(win)
    mouth=Oval(Point(30,90), Point (50,85))
    mouth.setFill('black')
    mouth.draw(win)
    win.getMouse()
    eye3=Circle(Point(30, 105), 5)
    eye3.setFill('orange')
    eye3.draw(win)
    eye4=Circle(Point(45,105), 5)
    eye4.setFill('yellow')
    eye4.draw(win)

main()


