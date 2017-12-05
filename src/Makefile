
HOST := $(shell hostname)
ifeq ($(HOST),cisc360)
RUN = srun -c 10
else
RUN = 
all: clean build
	$(RUN) python main.py
clean:
	rm -rf *.pyc *.so cy_quicksort.c ./build/* ./build
build: Makefile
	python setup.py build_ext --inplace
	python omp_setup.py build_ext --inplace