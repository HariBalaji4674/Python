'''
Compare two elements each time 
Swap if any elements are in wrong order

Select only two elements to compare 


Selection Sort Implementation:
- Select and sort the elements with unsorted elemenets
- 
-   
'''


def bubble_sort(arr):
    n = len(arr)
    # return n
    for i in range(0,n):
        # return arr[i]
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


unlisted_array = [5,7,8,2,10,3,4,6,1,9]
sorted_list = bubble_sort(unlisted_array)
print(sorted_list)

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min  = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

unselected_list = [5,7,8,2,10,3,4,6,1,9]
sorted_list = selection_sort(unselected_list)
print(sorted_list)

# class 














