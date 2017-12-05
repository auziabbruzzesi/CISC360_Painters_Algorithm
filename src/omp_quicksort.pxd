#//Quick sort implementation found on StackOverflow
#//https://stackoverflow.com/questions/36503828/cython-memoryviews-wrapping-c-function-with-array-parameter-to-pass-numpy-array
cdef extern from "omp_quicksort.h":
    void omp_quick_sort (int* a, int n)