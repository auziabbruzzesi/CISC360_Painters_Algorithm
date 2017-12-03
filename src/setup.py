from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['cy_quicksort.pyx', 'quicksort.c']

extensions = [Extension("cy_quicksort", sourcefiles)]

setup(
    ext_modules = cythonize(extensions)
)
