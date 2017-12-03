from factory import*
from graphics import*
from cy_quicksort import *
from quicksort import *
import Gnuplot
import numpy as np
import time
import random
sys.setrecursionlimit(1500)
#win = GraphWin("My Circle", 1000, 1000)

g = Gnuplot.Gnuplot(persist=0)
x = [16,32,64,128]
y = []
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

print("generating trial 5")
dict5=generate_shape_dictionary(256)
zval_python5 = np.array(list(dict5.keys()),dtype=np.int32)
zval_python_c5 = zval_python5[:]
zval_python_omp5 = zval_python_c5[:]
print("done \n")

print("generating trial 6")
dict6=generate_shape_dictionary(512)
zval_python6 = np.array(list(dict6.keys()),dtype=np.int32)
zval_python_c6 = zval_python6[:]
zval_python_omp6 = zval_python_c6[:]
print("done \n")

print("generating trial 7")
dict7=generate_shape_dictionary(1024)
zval_python7 = np.array(list(dict7.keys()),dtype=np.int32)
zval_python_c7 = zval_python7[:]
zval_python_omp7 = zval_python_c7[:]
print("done \n")


print("generating trial 8")
dict8=generate_shape_dictionary(2048)
zval_python8 = np.array(list(dict8.keys()),dtype=np.int32)
zval_python_c8 = zval_python8[:]
zval_python_omp8 = zval_python_c8[:]
print("done \n")


print("generating trial 9")
dict9=generate_shape_dictionary(4096)
zval_python9 = np.array(list(dict9.keys()),dtype=np.int32)
zval_python_c9 = zval_python9[:]
zval_python_omp9 = zval_python_c9[:]
print("done \n")

print("generating trial 10")
dict10=generate_shape_dictionary(8192)
zval_python10 = np.array(list(dict10.keys()),dtype=np.int32)
zval_python_c10 = zval_python10[:]
zval_python_omp10 = zval_python_c10[:]
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

y.append(pytime)
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
y.append(pytime2)
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
y.append(pytime3)
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
y.append(pytime4)
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
# d = Gnuplot.Data(x,y,with_= 'l',title='test')
# g.plot(d)

# for i in zval_python_c4:
#     for j in dict4.get(i):
#         j.getGraphic().setFill(random.choice(colors))
#         j.getGraphic().draw(win)
#         time.sleep(.08)

# win.getMouse() # Pause to view result
# win.close()    # Close window when done


##############################################TRIAL 5#############################################################
print("##########Timing Trial 5##########\n\n")
#print(zval_python2)
start = time.time()
zval_python5= quickSort(zval_python5)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime5 = end-start
y.append(pytime5)
print(pytime5)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c5)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc5 = end - start
print(pyplusc5)

print("speedup"),
print(pytime5/pyplusc5)
print("\n\n")

##############################################TRIAL 5#############################################################
print("##########Timing Trial 6##########\n\n")
#print(zval_python2)
start = time.time()
zval_python6= quickSort(zval_python6)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime6 = end-start
y.append(pytime6)
print(pytime6)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c6)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc6 = end - start
print(pyplusc6)

print("speedup"),
print(pytime6/pyplusc6)
print("\n\n")

##############################################TRIAL 7#############################################################
print("##########Timing Trial 7##########\n\n")
#print(zval_python2)
start = time.time()
zval_python7= quickSort(zval_python7)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime7 = end-start
y.append(pytime7)
print(pytime7)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c7)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc7 = end - start
print(pyplusc7)

print("speedup"),
print(pytime7/pyplusc7)
print("\n\n")

##############################################TRIAL 8#############################################################
print("##########Timing Trial 8##########\n\n")
#print(zval_python2)
start = time.time()
zval_python8= quickSort(zval_python8)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime8 = end-start
y.append(pytime8)
print(pytime8)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c8)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc8 = end - start
print(pyplusc8)

print("speedup"),
print(pytime8/pyplusc8)
print("\n\n")

##############################################TRIAL 9#############################################################
print("##########Timing Trial 9##########\n\n")
#print(zval_python2)
start = time.time()
zval_python9= quickSort(zval_python9)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime9 = end-start
y.append(pytime9)
print(pytime9)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c9)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc9 = end - start
print(pyplusc9)

print("speedup"),
print(pytime9/pyplusc9)
print("\n\n")

##############################################TRIAL 10#############################################################
print("##########Timing Trial 10##########\n\n")
#print(zval_python2)
start = time.time()
zval_python10= quickSort(zval_python10)
end = time.time()
#print(zval_python2)
print("TIME FOR JUST PYTHON:"),
pytime10 = end-start
y.append(pytime10)
print(pytime10)


#print(zval_python_c2)
start = time.time()
quicksort_c(zval_python_c10)
end = time.time()
#print(zval_python2)
print("TIME FOR PYTHON+C:"),
pyplusc10 = end - start
print(pyplusc10)

print("speedup"),
print(pytime10/pyplusc10)
print("\n\n")