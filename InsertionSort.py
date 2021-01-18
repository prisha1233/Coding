### Insertion Sort

#### time complexity is O (n^2)

def insertionSort(arr):

    n =len(arr)
    for i in range(1,n):

        key = arr[i]
        j = i-1

        while (j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key

    return arr


arr = [45,78,34,2,5,89,67,80]

print (insertionSort(arr))

