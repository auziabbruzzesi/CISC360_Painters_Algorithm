#//Quick sort implementation found on StackOverflow
#//https://stackoverflow.com/questions/36503828/cython-memoryviews-wrapping-c-function-with-array-parameter-to-pass-numpy-array
cdef extern from "quicksort.h":
    void quick_sort (int* a, int n)