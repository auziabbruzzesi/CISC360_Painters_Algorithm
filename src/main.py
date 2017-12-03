from factory import*
from graphics import*
from cy_quicksort import *
from quicksort import *
import numpy as np
import time
import random
sys.setrecursionlimit(1500)
win = GraphWin("My Circle", 1000, 1000)

colors = ["Green","Blue","Orange","yellow","red","pink","white","gold"]
#generate the dictionaries
print("generating trial 1")
dict1=generate_shape_dictionary(16)
zval_python1 = np.array(list(dict1.keys()),dtype=np.int32)
zval_python_c1 = zval_python1[:]
zval_python_omp1 = zval_python_c1[:]

print("done\n")

print("generating trial 2")
dict2=generate_shape_dictionary(32)
zval_python2 = np.array(list(dict2.keys()),dtype=np.int32)
zval_python_c2 = zval_python2[:]
zval_python_omp2 = zval_python_c2[:]
print("done \n")

print("generating trial 3")
dict3=generate_shape_dictionary(64)
zval_python3 = np.array(list(dict3.keys()),dtype=np.int32)
zval_python_c3 = zval_python3[:]
zval_python_omp3 = zval_python_c3[:]
print("done \n")

print("generating trial 4")
dict4=generate_shape_dictionary(128)
zval_python4 = np.array(list(dict4.keys()),dtype=np.int32)
zval_python_c4 = zval_python4[:]
zval_python_omp4 = zval_python_c4[:]
print("done \n")

print("TIME TRIALS_______________________________\n_________________________________________________________________")

##############################################TRIAL 1#############################################################
print("###########Timing Trial 1#########\n\n")
#print(zval_python1)
start = time.time()
zval_python1 = quickSort(zval_python1)
end = time.time()
#print(zval_python1)
print("TIME FOR JUST PYTHON:"),
pytime = end-start
print(pytime)

#print(zval_python_c1)
start = time.time()
quicksort_c(zval_python_c1)
end = time.time()
#print(zval_python1)
print("TIME FOR PYTHON+C:"),
pyplusc = end - start
print(pyplusc)

print("speedup"),
print(pytime/pyplusc)
print("\n\n")
##############################################TRIAL 2#############################################################
print("##########Timing Trial 2##########\n\n")
#print(zval_python2)
start = time.time()
zval_python2 = quickSort(zval_python2)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime2 = end-start
print(pytime2)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c2)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc2 = end - start
print(pyplusc2)

print("speedup"),
print(pytime2/pyplusc2)
print("\n\n")

##############################################TRIAL 3#############################################################
print("##########Timing Trial 3##########\n\n")
#print(zval_python2)
start = time.time()
zval_python3 = quickSort(zval_python3)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime3 = end-start
print(pytime3)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c3)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc3 = end - start
print(pyplusc3)

print("speedup"),
print(pytime3/pyplusc3)
print("\n\n")

##############################################TRIAL 4#############################################################
print("##########Timing Trial 4##########\n\n")
#print(zval_python2)
start = time.time()
zval_python4 = quickSort(zval_python4)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime4 = end-start
print(pytime4)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c4)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc4 = end - start
print(pyplusc4)

print("speedup"),
print(pytime4/pyplusc4)
print("\n\n")


for i in zval_python_c4:
    for j in dict4.get(i):
        j.getGraphic().setFill(random.choice(colors))
        j.getGraphic().draw(win)
        time.sleep(.08)

win.getMouse() # Pause to view result
win.close()    # Close window when done