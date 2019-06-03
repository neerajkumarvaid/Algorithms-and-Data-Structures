# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:15:03 2019

@author: Neeraj

Lecture 1 : Peak finding algorithm for 2D arrays

"""


def global_max(array):
    """ This function finds the global maximum of 1D array.
    This will be required in a 2D peak finding algorithm to
    find global maximum of a column.
    Input: A 1D array of values
    Output: Global maximum of the array.
    Complexity: O(n)"""
    
    # Intialize maximum index and value
    max_index = 0
    max_value = array[max_index]
    for index, element in enumerate(array):
        if element > max_value:
            max_index = index
            max_value = element
    return max_index
    
    
    

def peak2d(array):
    '''This function finds the peak in a 2D array by the
       recursive method.

       Complexity: O(n log m)'''
       
    m = len(array[0]) # number of columns

    j = m//2 # Select the middle column

    row = [i[j] for i in array] # Extract the entire middle column

    #i = row.index(max(row)) # Find index of the  global maximum of the column
    i = global_max(row) # Find index of the  global maximum of the column
    #print array[i][j] # print the global maximum of the column

# Check the neighborhood of the global maximum to find a peak
    if j >0 and j < m-1 and array[i][j] < array[i][j-1] and array[i][j] < array[i][j+1]:
        if array[i][j-1] < array[i][j+1]:
            return peak2d([row[j:] for row in array])
        else:
            return peak2d([row[:j] for row in array])

    elif j > 0 and array[i][j] < array[i][j-1]: #
        return peak2d([row[:j] for row in array])

    elif j < m - 1 and array[i][j] < array[i][j+1]:
        return peak2d([row[j:] for row in array])

    else:
        return array[i][j]
        
array = [[4,6,3,5,1,8],
         [14, 5, 3, 29,2, 7],
         [5,2,6,9,13,41,8]]       
        
print peak2d(array)
