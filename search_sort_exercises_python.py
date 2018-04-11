"""
1. Write a Python program for binary search. 
Binary Search : In computer science, a binary search or half-interval search
algorithm finds the position of a target value within a sorted array. The binary
search algorithm can be classified as a dichotomies divide-and-conquer search
algorithm and executes in logarithmic time.
Test Data :
binary_search([1,2,3,5,8], 6) -> False
binary_search([1,2,3,5,8], 5) -> True
"""

def binary_search(data, x):
    data.sort()
    low = 0
    high = len(data)-1
    while low<=high:
        mid = int((high+low)/2)
        n = data[mid]
        if x == n:
            return True
        elif x < n:
            high = mid-1
        else:
            low = mid+1
    return False
        
print(binary_search([1,2,3,5,8], 6))          
print(binary_search([3,4,8,1,5], 5)) 

"""
2. Write a Python program for sequential search.
Sequential Search : In computer science, linear search or sequential search is
a method for finding a particular value in a list that checks each element in
sequence until the desired element is found or the list is exhausted.
The list need not be ordered.
Test Data :
Sequential_Search([11,23,58,31,56,77,43,12,65,19],31) -> (True, 3)
"""

def sequential_search(data, x):
    for item in data:
        if x == item:
            return True, data.index(item)
    else:
        return False, -1

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))

"""
3. Write a Python program for binary search for an ordered list. 
Test Data :
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3) -> True
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17) -> False
"""

def ordered_binary_search(data, x):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((high+low)/2)
        n = data[mid]
        if x == n:
            return True
        elif x < n:
            high = mid-1
        else:
            low = mid+1
    return False

print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))

"""
4. Write a Python program to sort a list of elements using the bubble sort
algorithm. 
Note : According to Wikipedia "Bubble sort, sometimes referred to as sinking
sort, is a simple sorting algorithm that repeatedly steps through the list to
be sorted, compares each pair of adjacent items and swaps them if they are in
the wrong order. The pass through the list is repeated until no swaps are needed
, which indicates that the list is sorted. The algorithm, which is a comparison
sort, is named for the way smaller elements "bubble" to the top of the list.
Although the algorithm is simple, it is too slow and impractical for most
problems even when compared to insertion sort. It can be practical if the input
is usually in sort order but may occasionally have some out-of-order elements
nearly in position."
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]
"""

def bubble_sort(data):
    swaps = 1
    while swaps:
        n = 0
        while n < len(data)-1:
            if data[n]>data[n+1]:
                temp = data[n]
                data[n] = data[n+1]
                data[n+1] = temp
                swaps += 1
            n += 1
        if swaps > 1:
            swaps = 1
        else:
            swaps = 0   
    return data        

print(bubble_sort([14,46,43,27,57,41,45,21,70]))

"""
5. Write a Python program to sort a list of elements using the selection sort
algorithm. 
Note : The selection sort improves on the bubble sort by making only one
exchange for every pass through the list. 
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]
"""

def selection_sort(data):
    for i in range(len(data), 0, -1):
        local_max = max(data[:i])
        max_index = data.index(local_max)
        temp = data[i-1]
        data[i-1] = local_max
        data[max_index] = temp
    return data
        
print(selection_sort([14,46,43,27,57,41,45,21,70]))

"""
6. Write a Python program to sort a list of elements using the insertion sort
algorithm. 
Note : According to Wikipedia "Insertion sort is a simple sorting algorithm
that builds the final sorted array (or list) one item at a time. It is much
less efficient on large lists than more advanced algorithms such as quicksort,
heapsort, or merge sort."
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70]
"""

def insertion_sort(data):
    for i in range(len(data)):
        loc = i
        for j in range(i-1, 0, -1):     
            if data[j]>data[loc] and loc>=0:
                temp = data[loc]
                data[loc] = data[j]
                data[j] = temp
                loc -= 1
    return data

print(insertion_sort([14,46,43,27,57,41,45,21,70]))
