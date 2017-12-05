from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['omp_cy_quicksort.pyx', 'omp_quicksort.c']

extensions = [Extension("omp_cy_quicksort", sourcefiles,extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'])]

setup(
    ext_modules = cythonize(extensions)
)
