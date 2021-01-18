
### BUBBLE SORT
### TIME COMPLEXITY IS O(N^2)
### sort biggest to smallest


def bubbleSort(arr):
    n = len(arr)
    for i in range(0, len(arr)):

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print (arr)

    return arr


arr = [45, 78, 34, 2, 5, 89, 67, 80]

print (bubbleSort(arr))