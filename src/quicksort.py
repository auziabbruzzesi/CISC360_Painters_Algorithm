def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quickSort(less)+equal+quickSort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array




# def quickquickSort(arr):
#     less = []
#     pivotList = []
#     more = []
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         for i in arr:
#             if i < pivot:
#                 less.append(i)
#             elif i > pivot:
#                 more.append(i)
#             else:
#                 pivotList.append(i)
#         less = quickquickSort(less)
#         more = quickquickSort(more)
#         return less + pivotList + more
        