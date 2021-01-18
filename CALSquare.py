#  merging sort
def mergingSort (arr):

    if (len(arr)> 1):

        mid = len(arr)//2

        left = arr[:mid]
        right= arr[mid:]

        mergingSort(left)
        mergingSort(right)

        i=j=k=0

        while (i < len(left) and j < len(right)):

            if left[i] < right[j]:
                arr[k]= left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1


        ##### check whether any element missed or not

        while (i < len(left)):
            arr[k] = left[i]
            i+=1
            k+=1

        while (j < len(right)):
            arr[k] = right[j]
            j+=1
            k+=1



arr = [45, 78, 34, 2, 5, 89, 67, 80]
print ("Unsorted array : ", arr)
mergingSort(arr)

print ("This program has been follow divide and conqueor algorithm. MERGING SORT time complexity is o(nlogn)")
print ("sorte array : ",arr)