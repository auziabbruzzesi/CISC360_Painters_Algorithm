from factory import*
from graphics import*
from cy_quicksort import *
from quicksort import *
import Gnuplot
import numpy as np
import time
import random
import timeit
sys.setrecursionlimit(1500)
#win = GraphWin("My Circle", 1000, 1000)

# g = Gnuplot.Gnuplot(persist=0)
# x = [16,32,64,128]
# y = []
colors = ["Green","Blue","Orange","yellow","red","pink","white","gold"]
#generate the dictionaries

def generate(num_shapes):
   # print("generating trial "),
    #print(num_shapes)
    dicta=generate_shape_dictionary(num_shapes)
    zval_python = np.array(list(dicta.keys()),dtype=np.int32)
    zval_python_c = zval_python[:]
    zval_python_omp = zval_python_c[:]
    #print("done \n")
    return(zval_python,zval_python_c,zval_python_omp)


def time_trial(num_shapes):
    tup = generate(num_shapes)
    print("done generating...")
    zval_python = tup[0]
    zval_python_c = tup[1]
    zval_python_omp = tup[2]

    def time_py():
        quickSort(zval_python)
    def time_py_c():
        quicksort_c(zval_python_c)
    def time_py_omp():
        return 0
    
    tp = timeit.Timer(time_py)
    tpc = timeit.Timer(time_py_c)
    avgtp = tp.timeit(500)/500
    avgtpc = tpc.timeit(500)/500
    #tpo = timeit.Timer(time_py_omp)
   
    print(num_shapes)

    return(avgtp,avgtpc)
    

for i in range(13):
    tup =time_trial(2**i)
    print("JUST PY"),
    print(tup[0])
    print("PY + C"),
    print(tup[1])
    print("SPEEDUP---"),
    print(tup[0]/tup[1])
    print("\n\n\n")



