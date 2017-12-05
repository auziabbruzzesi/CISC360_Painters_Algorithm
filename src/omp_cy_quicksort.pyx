#//Quick sort implementation found on StackOverflow
#//https://stackoverflow.com/questions/36503828/cython-memoryviews-wrapping-c-function-with-array-parameter-to-pass-numpy-array
cimport omp_quicksort

def omp_quicksort_c(int[::1] a):
    omp_quicksort.omp_quick_sort(&a[0], a.size)