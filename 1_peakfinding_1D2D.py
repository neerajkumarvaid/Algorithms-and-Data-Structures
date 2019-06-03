# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 00:59:28 2019

@author: Neeraj

Lecture 1 : Peak finding algorithm for 1D and 2D arrays
"""

def peak1d(array):
    '''This function recursively finds the peak in an array
       by dividing the array into 2 repeatedly and choosning
       sides.

       Complexity: O(log n)'''

    start, stop = 0, len(array) # bounds for binary search
    while True:
        mid = (start + stop) // 2 # middle element 
        if mid > 0 and array[mid] < array[mid-1]: # comparison of the mid
            stop = mid # select the left leg of the array
        elif mid < len(array) - 1 and array[mid] < array[mid+1]: # comparison of the mid
            start = mid # Select the right leg of the array
        else:
            return array[mid] # return if mid is the peak
   
# Run an example of 1D peak finding algorith,         
array = [1, 3, 4, 3, 5, 1, 3]

print peak1d(array)

def peak2d(array):
    '''This function finds the peak in a 2D array by the
       recursive method.

       Complexity: O(n log m)'''
       
    m = len(array[0]) # number of columns

    j = m//2 # Select the middle column

    row = [i[j] for i in array] # Extract the entire middle column

    i = row.index(max(row)) # Find global maximum of the column

    print(i, j) # print the global maximum of the column

# Check the neighborhood of the global maximum to find a peak
    if j > 0 and array[i][j] < array[i][j-1]: #
        return peak2d([row[:j] for row in array])

    elif j < m - 1 and array[i][j] < array[i][j+1]:
        return peak2d([row[j:] for row in array])

    else:
        return array[i][j]
        
array = [[4,6,3,5,1,8],
         [14, 5, 3, 29,2, 7],
         [5,2,6,9,13,41,8]]       
        
print peak2d(array)
        