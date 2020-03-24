#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:08:03 2020

@author: Neeraj

Lecture 3: Insertion and Merge Sort
"""
from typing import List

def insertion_sort(data: List[int]) -> List[int]:
    """input: Unsorted list of integers
       output: Sorted list of intergers
    """
    for i in range(1,len(data)):
        print(f"data at iteration {i} = {data}")
        while i:
            key = data[i]
        
            if key < data[i-1]:
            
                data[i] = data[i-1]
                data[i-1] = key
            i -= 1
            
    return data

data = [5,2,4,6,1,3] # input list
sdata = insertion_sort(data) # sorted list
print(f"The sorted list is {sdata}")

data = [5,2,2,1,1,0]
sdata = insertion_sort(data)
print(f"The sorted list is {sdata}")

def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q+1+j]
    #L[n1+1] = float('inf')
    #L[n2+1] = float('inf')
    
            
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = p     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            A[k] = L[i] 
            i += 1
        else: 
            A[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        A[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        A[k] = R[j] 
        j += 1
        k += 1
        
    return A
             
def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A

A = [5,2,4,6,1,3] # input list
sA = merge_sort(A, 0, len(A)-1) # sorted list
print(f"The sorted list is {sA}")