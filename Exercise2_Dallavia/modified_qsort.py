"""
Ryan C. Dallavia
06/12/2018
CS242 - Summer Session
Exercise 2

The following represents an adjustment to the quickSort routine found in
Lambert, Kenneth A. (2014)  "Fundamentals of Python: Data Structures".  
Specifically, the modified quickSort (modified_qsort) was added, which calls
insertion sort on any sublist whose size is less than 50 items. Benchmarking data
are compared between it and Lambert's original quickSort implementation.
Note, the student's implementations of quickSort and insertion sort tend to be 
more laconic.
"""


from algorithms import insertionSort

# added profiler to external and internal headers
def mod_quicksort(lyst, profiler):
    '''
    Runs quicksort unless sublist size falls below specified threshold,
    in which case routine invokes insertionSort
    '''
    quicksortHelper(lyst, 0, len(lyst) - 1, profiler)

# added profiler & threshold to external and internal headers
def quicksortHelper(lyst, left, right, profiler):
    '''
    Modified to utilize insertion sort when subsegment length
    was strictly less than specified threshold. 
    '''
    # subsegment length below which program switches from quickSort to 
    # insertionSort
    threshold = 50
    profiler.comparison()
    if left < right:
        profiler.comparison()
        if right - left < threshold:
            insertionSort(lyst, profiler)
        else:
            pivotLocation = partition(lyst, left, right, profiler)
            quicksortHelper(lyst, left, pivotLocation - 1, profiler)
            quicksortHelper(lyst, pivotLocation + 1, right, profiler)

def partition(lyst, left, right, profiler):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    profiler.exchange()
    lyst[right] = pivot
    profiler.exchange()
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        profiler.comparison()
        if lyst[index] < pivot:
            swap(lyst, index, boundary, profiler)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary, profiler)
    return boundary

def swap(lyst, i, j, profiler):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    profiler.exchange()
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp



