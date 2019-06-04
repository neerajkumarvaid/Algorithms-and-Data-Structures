# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:13:45 2019

@author: Neeraj
Lecture 1 : Peak finding algorithm for 1D

"""

def peak1d(array):
    '''This function recursively finds a peak in an array by 
    repeatedly dividing the array into 2 sub-arrays until 
    a peak is found.
    Complexity: O(log n)'''
    start, stop = 0, len(array) # bounds for binary search
    mid = (start + stop) // 2 # middle element 
    
    # If lenght of the array is 1 then return the only element in the array
    if len(array) == 1:
        return array[mid]
    # If the length of the array is 2 then return the max of two elements
    elif len(array) == 2:
        return max(array)
    # If array contains at least three elements then check if the middle element is smaller than both of its neighbors
    if array[mid+1] > array[mid] and array[mid] < array[mid-1]:
        # Update start if the right neighbor is greater than the left neighbor of the middle element
        if array[mid+1] > array[mid-1]:
            start = mid + 1
            #print start, array[start:]
            # Run algorithm on the right-subarray
            return peak1d(array[start:])
        else:
            # Update stop if the left neighbor is greater than the right neighbor of the middle element
            stop = mid-1
            #print stop, array[:stop+1]
            return peak1d(array[:stop+1])
    # If array contains at least three elements then check if the middle element is smaller than its right neighbor
    elif array[mid+1] > array[mid]:
        # Update start
        start = mid + 1
        # Run algorithm on the right sub-array
        return peak1d(array[:stop+1])
    # If array contains at least three elements then check if the middle element is smaller than its left neighbor
    elif array[mid+1] > array[mid]:
        # Update start
        stop = mid-1
        # Run algorithm on the left sub-array
        return peak1d(array[start:])
    else:
        return array[mid]
        
# Run an example of 1D peak finding algorith,         
array = [1, 3, 4, 3, 5, 1, 3]

print peak1d(array)
