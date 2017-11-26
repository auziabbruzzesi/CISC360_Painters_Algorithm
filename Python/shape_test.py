from graphics import *
from quicksort import *
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
    c.setFill("red")
    c2 = Circle(Point(55,55), 10)
    c2.setFill("blue")
    red = Shape(c,20)
    blue = Shape(c2,10)
    
    shapes = [red, blue]

    sorted = quickSort(shapes)

    for sort in sorted:
    	sort.getGraphic().draw(win)
    	time.sleep(2)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()