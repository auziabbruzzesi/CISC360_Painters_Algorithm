cimport omp_quicksort

def omp_quicksort_c(int[::1] a):
    omp_quicksort.omp_quick_sort(&a[0], a.size)