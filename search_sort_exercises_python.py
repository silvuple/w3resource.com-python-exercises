"""
SEARCH
"""

"""
1. Write a Python program for binary search. 
"""

# solution 1 (changing location of 'mid' item untill 'first' and 'last' are the same item)
def binary_search(my_list, x):
    first = 0
    last = len(my_list)-1
    while first <= last:
        mid = (first+last)//2
        if x == my_list[mid]:
            return True
        elif x > my_list[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return False

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 1))

# solution 2 (similar to 1, slicing the list untill list length is 0)
def binary_search(my_list, x):
    while len(my_list) > 0:
        last = len(my_list)-1
        mid = last//2
        if x == my_list[mid]:
            return True
        elif x > my_list[mid]:
            my_list = my_list[mid+1:]
        else:
            my_list = my_list[:mid]
    return False

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 1))

# solution 3 (with recursion)
def binary_search(my_list, x):
    if len(my_list) == 0:
        return False
    mid = len(my_list)//2
    if x == my_list[mid]:
        return True
    elif x > my_list[mid]:
        return binary_search(my_list[mid+1:], x)
    else:
        return binary_search(my_list[:mid], x)

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 1))

"""
2. Write a Python program for sequential search. 
"""

def sequential_search(my_list, x):
    for item in my_list:
        if item == x:
            return True
    return False

print(sequential_search([11,23,58,31,56,77,43,12,65,19], 11))

"""
SORT
"""

"""
4. Write a Python program to sort a list of elements using the bubble sort algorithm.
"""

# solution 1
def buble_sort(my_list):
    # counting number of "no_swap" pairs (naigbors that are in the right order),
    # when list is sorted the number of "no_swaps" will equal to len(list)-1
    # for each "walk" through the list, the "no_swaps" number is reset back to 0
    
    no_swaps = 0
    while no_swaps < (len(my_list)-1):
        no_swaps = 0
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp
            else:
                no_swaps += 1

x = [14,46,43,27,57,41,45,21,70,15]
buble_sort(x)
print(x)
y = [5,1,4,2,8]
buble_sort(y)
print(y)

"""
5. Write a Python program to sort a list of elements using the selection sort algorithm.
"""

def selection_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        maximum = max(my_list[:i])
        max_ind = my_list.index(maximum)
        if maximum > my_list[i]:
            temp = maximum
            my_list[max_ind] = my_list[i]
            my_list[i] = temp
            
x = [14,46,43,27,57,41,45,21,70,15]
selection_sort(x)
print(x)
y = [5,1,4,2,8]
selection_sort(y)
print(y)

"""
6. Write a Python program to sort a list of elements using the insertion sort algorithm.
"""

def insertion_sort(my_list):
    # for each element in the list (first for loop), we compare it to each of the
    # preciding elements (second for loop), and move it to it's sorted position
    # relative to it's preciding elements; this way for each next element 
    # the elements before it are already in the correct sorted order
    for i in range(1,len(my_list)):
        loc = i
        for j in range(i-1,-1,-1):
            if  my_list[loc] < my_list[j]:
                temp = my_list[loc]
                my_list[loc] = my_list[j]
                my_list[j] = temp
                loc = j
              
x = [14,46,43,27,57,41,45,21,70,15]
insertion_sort(x)
print(x)
y = [5,1,4,2,8]
insertion_sort(y)
print(y)

"""
7. Write a Python program to sort a list of elements using shell sort algorithm.
"""

def shell_sort(my_list):
    # each gap is the "sublist", i.e. gap=1 is the whole list, gap = 2 is half the list elements etc.
    gap = len(my_list)//2
    while gap > 0:
        print("gap=",gap)
        print("before this gap sort", my_list)
        # for each element in the list (first for loop), compare it to every
        # preciding elements of it's "sublist" (second for loop).
        # "sublist" is defined by "gap"
        for i in range(gap,len(my_list)):
            print('i=',i)
            loc = i
            for j in range(i-gap, -1, -gap):
                if  my_list[loc] < my_list[j]:
                    temp = my_list[loc]
                    my_list[loc] = my_list[j]
                    my_list[j] = temp
                    loc = j
                    print(my_list)
        gap = gap//2
        print(">",my_list)
        
x = [89,14,46,43,27,57,41,45,21,70,15,1,90]
shell_sort(x)
print(x)
y = [5,1,4,2,8]
shell_sort(y)
print(y)

"""
8. Write a Python program to sort a list of elements using the merge sort algorithm.
"""
# solution from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0 
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            
        # elements on leftside that were left "unmerged"
        #(because they are bigger than the rest)
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
            
        # elemnts on rightside that were left "unmerged"
        #(because they are bigger than the rest)
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        
x = [14,46,43,27,57,41,45,21,70,15,1]
merge_sort(x)
print(x)
y = [5,1,4,2,8]
merge_sort(y)
print(y)

"""
9. Write a Python program to sort a list of elements using the quick sort algorithm.
"""

def quick_sort(my_list):
    
    def quick_sort_recur(my_list, start, end):
        # inner helper function to help perform the quick sort recursively each
        # time updating the start and end of the 'working section' of the list

        # check if the 'working section' of the list (from 'start' to 'end' index)
        # has more than 1 element, otherwise it is already 'sorted'
        if start < end:
            
            pivot_ind = start           # pivot value index
            left_ind = pivot_ind + 1    # leftside, start index 
            right_ind = end             # rightside, end index

            # check untill the left and right indexes cross, i.e. untill all the
            # elements of the section are checked and moved if needed
            while left_ind <= right_ind:
                
                # if leftside value is lower than pivot value,
                # move left index one place to the right
                if my_list[left_ind] < my_list[pivot_ind]:
                    left_ind += 1
                    
                # if rightside value is higher than pivot value,
                # move right index one place to the left
                elif my_list[right_ind] > my_list[pivot_ind]:
                    right_ind -= 1
                    
                # if leftside value is higher and rightside is lower than
                # pivot value, swap the left and right values, and move both
                # indexes inward
                else:
                    temp = my_list[left_ind]
                    my_list[left_ind] = my_list[right_ind]
                    my_list[right_ind] = temp
                    left_ind += 1
                    right_ind -= 1

            # when right and left indexes have crossed (section is finished),
            # move the pivot value to separate left(lower values side) and
            # right(higher values side)
            temp = my_list[pivot_ind]
            my_list[pivot_ind] = my_list[right_ind]
            my_list[right_ind] = temp

            # repeat for leftside of the pivot value, the end of the new section
            # is where the pivot value was moved not including (right index - 1), 
            # there is no need to include it as it is already in its right
            # position in the sorted list
            quick_sort_recur(my_list, pivot_ind, right_ind-1)
            
            # repeat for rightside of the pivot value, the beginning of the new section
            # is where the pivot value was moved not inlcuding (right index + 1)
            quick_sort_recur(my_list, right_ind+1, end)

    # first call to the quick_sort_recut function with the start=0 and end=last index of the list         
    quick_sort_recur(my_list, 0, len(my_list)-1)            
        
x = [48,14,46,43,21,57,41,45,27,70,15,1]
quick_sort(x)
print(x)
y = [5,1,4,2,8]
quick_sort(y)
print(y)
            
"""
10. Write a Python program for counting sort.
"""
# helped me to solve very easily: https://brilliant.org/wiki/counting-sort/

def counting_sort(my_list):
    # 'counter' is the list that for each integer element of 'my_list' will store
    # the number of times this integer appears in 'my_list' + number of inetgers that
    # are lower than this integer, so each integer must have index == this integer in 'counter'
    counter = [0] * (max(my_list)+1)

    # 'out' is the final sorted 'my_list' the function will return, it must have same length
    out = [0] * len(my_list)

    # the number of times each integer appears in 'my_list' is stored in counter
    # under index that equals to this integer
    for i in my_list:
        counter[i] += 1

    # each element in counter is incremented by the sum of all the preceding elements
    for i in range(1, len(counter)):
        counter[i] = counter[i] + counter[i-1]

    # each inetger starting from the end of my_list is added to the 'out' list
    # at the index position determined by the value that is stored in 'counter' list
    # under the index == this integer element
    # the value in 'counter' is reduced by 1, as one slot is taken
    for i in my_list[::-1]:
        ind = counter[i]-1
        out[ind] = i
        counter[i] -= 1
    
    return out

x = [48,14,46,43,21,57,41,45,27,70,15,1]
print(counting_sort(x))
y = [5,1,4,2,8]
print(counting_sort(y))
