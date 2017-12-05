cdef extern from "omp_quicksort.h":
    void omp_quick_sort (int* a, int n)