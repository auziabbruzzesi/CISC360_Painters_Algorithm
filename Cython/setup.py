from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("quicksort.pyx")
)
#will need to declare omp stuff here