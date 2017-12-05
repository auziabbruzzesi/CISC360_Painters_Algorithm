#//Quick sort implementation found on StackOverflow
#//https://stackoverflow.com/questions/36503828/cython-memoryviews-wrapping-c-function-with-array-parameter-to-pass-numpy-array
cimport quicksort

def quicksort_c(int[::1] a):
    quicksort.quick_sort(&a[0], a.size)