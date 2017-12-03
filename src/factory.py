# Factory/shapefact1/ShapeFactory1.py
# A simple static factory method.
from __future__ import generators
from graphics import *
import random as r

class Shape:
    def __init__(self, graphic, zval):
	    self.zval = zval
	    self.graphic = graphic
    def printZval(self): print(self.zval)
    def getZval(self): return self.zval
    def getGraphic(self): return self.graphic
    r.seed(15)
    # Create based on class name:
    def factory(type):
        
        
        #return eval(type + "()")
        if type == "Circle": 
            randx = r.randint(0,1000)
            randy = r.randint(0,1000)
            randr = r.randint(6,100)
            randz = r.randint(-1000,0)
            return Shape(Circle(Point(randx,randy),randr),randz)
        elif type == "Rectangle":
            randx = r.randint(0,500)
            randy = r.randint(0,800)
            randx2 = randy
            randy2 = randx
            randz =r.randint(-1000,0)

            return Shape(Rectangle(Point(randx,randy),Point(randx2,randy2)),randz)

            
            
        #if type == "Square": return Square()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)


def shapeNameGen(n):
    types = ["Circle"]#,"Rectangle"]
    for i in range(n):
        yield r.choice(types)

def generate_shape_dictionary(n):
    print("\tpopulating dictionary")
    #print("GENERATING SHAPE DICTIONARY....."),
    shapes = dict()
    k = 1
    for i in shapeNameGen(n):
        a = Shape.factory(i)
        b = a.getZval()
        if b in shapes:
            shapes[b].append(a)
        else:
            shapes[b] = [a]
        # if k % 50000 == 0:
        #     print(n/k)
        # k+=1
            
           
    #print("DONE\n")
    print("\tdone")
    return shapes





#generate_shape_dictionary(1000000)