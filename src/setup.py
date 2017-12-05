#//Quick sort implementation found on StackOverflow
#//https://stackoverflow.com/questions/36503828/cython-memoryviews-wrapping-c-function-with-array-parameter-to-pass-numpy-array
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['cy_quicksort.pyx', 'quicksort.c']

extensions = [Extension("cy_quicksort", sourcefiles)]

setup(
    ext_modules = cythonize(extensions)
)
