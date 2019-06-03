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
    
    if mid >0 and array[mid+1] > array[mid] and array[mid] < array[mid-1]:
        if array[mid+1] > array[mid-1]:
            start = mid + 1
            #print start, array[start:]
            return peak1d(array[start:])
        else:
            stop = mid-1
            #print stop, array[:stop+1]
            return peak1d(array[:stop+1])
    elif mid >0 and array[mid+1] > array[mid]:
        start = mid + 1
        return peak1d2(array[:stop+1])
    elif mid >0 and array[mid+1] > array[mid]:
        stop = mid-1
        return peak1d(array[start:])
    else:
        return array[mid]
        
# Run an example of 1D peak finding algorith,         
array = [1, 3, 4, 3, 5, 1, 3]

print peak1d(array)
