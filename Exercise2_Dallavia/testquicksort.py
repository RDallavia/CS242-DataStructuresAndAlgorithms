"""
Ryan C. Dallavia
06/12/2018
CS242 - Summer Session
Exercise 2

The following is the quicksort routine found in
Lambert, Kenneth A. (2014)  "Fundamentals of Python: Data Structures". 
"""

def quicksort(lyst, profiler):
    quicksortHelper(lyst, 0, len(lyst) - 1, profiler)

def quicksortHelper(lyst, left, right, profiler):
    profiler.comparison()
    if left < right:
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

