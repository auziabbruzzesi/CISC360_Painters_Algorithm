#include <stdio.h>
#include<omp.h>


//void omp_quick_sort (int* a, int n) {

void omp_quick_sort(int *inputArray, int size){
	omp_set_num_threads(10);
	int pivot, leftIndex, rightIndex;
	/* End of reccursion */
	if (size <= 1) { return; }
	/* Set pivot */
	pivot = inputArray[size/2];
	for(leftIndex = 0, rightIndex = size -1;; leftIndex++, rightIndex--) {
		while(inputArray[leftIndex] < pivot){
			leftIndex++;
		}
		while(pivot < inputArray[rightIndex]){
			rightIndex--;
		}
		if(rightIndex <= leftIndex){
			break;
		}
		int temp;
	    temp = inputArray[leftIndex];
	    inputArray[leftIndex] = inputArray[rightIndex];
	    inputArray[rightIndex] = temp;    
	}
	#pragma omp task if(rightIndex-leftIndex > 1000)
	{
		omp_quick_sort(inputArray, leftIndex); /* Sort lower */
	}
	//#pragma omp task
	//{
		omp_quick_sort(inputArray + rightIndex + 1, size - rightIndex -1); /* Sort upper */
	//}
}