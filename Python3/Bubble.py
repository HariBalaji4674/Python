def bub_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

list1 = [78,65,50,76,43,23,33]
sord = bub_sort(list1)
print(sord)
























































































