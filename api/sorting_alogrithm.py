def bubble(arr1):
    n=len(arr1)
    swapped = False
    for i in range(n):
        for j in range(0,n-i-1):
            if arr1[j] > arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                swapped = True
        if not swapped:
            break
    return arr1    

def selection(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
                arr[i],arr[mini] = arr[mini],arr[i]
    return arr

def insertion(arr):
    n= len(arr)
    for i in range(1,n):
        key = arr[i]
        j= i-1
        while j>=0 and key< arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr  


def merge_sort(arr):
    #if the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left half
    result.extend(left[i:])

    # Append any remaining elements from the right half
    result.extend(right[j:])

    return result
