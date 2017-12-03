from graphics import *
from cy_quicksort import *
import numpy as np
import time

class Shape:
	def __init__(self, graphic, zval):
		self.zval = zval
		self.graphic = graphic
	def getZval(self): return self.zval
	def getGraphic(self): return self.graphic


def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    d = Circle(Point(60,60),10)
    d2 = Circle(Point(65,65),10)
    e = Circle(Point(70,70),10)
    e.setFill("gray")
    e2 = Circle(Point(75,75),10)
    e2.setFill("green")
    k = Circle(Point(80,80),10)
    k.setFill("orange")
    k2 = Circle(Point(85,85),10)
    k2.setFill("white")
    c.setFill("red")
    c2 = Circle(Point(55,55), 10)
    c2.setFill("blue")
    d.setFill("black")
    d2.setFill("magenta")
    red = Shape(c,10)
    blue = Shape(c2,20)
    b = Shape(d,35)
    s = Shape(d2,82)
    f = Shape(e,11)
    g = Shape(e2,437)
    h = Shape(k,98)
    i = Shape(k2,876)
    

    shapedict = dict()
    shapes = [red, blue,b,s,f,g,h,i]
    shapez = []
    # a = np.array(shapez,dtype=np.int32)

    for shape in shapes:
        print(shape.getZval())
        shapedict[shape.getZval()] = shape

    for i in shapedict:
        shapez.append(i)

    print("now shapedict")
    
    a = np.array(shapez,dtype=np.int32)
    print(shapedict)
    print(a)
    quickSort(a)
    print(a)
    
    
    for i in a:
    	shapedict.get(i).getGraphic().draw(win)
    	time.sleep(2)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()