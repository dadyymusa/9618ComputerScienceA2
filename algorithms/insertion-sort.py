arr = [90, 98, 67, 45, 32, 43, 12]

def InsertionSort(arr):
    for i in range(len(arr)):
        for n in range(len(arr) - i - 1):
            temp = arr[n + 1]
            if arr[n] > arr[n + 1]:
                arr[n + 1] = arr[n]
                arr[n] = temp
    return arr

InsertionSort(arr)
print(arr)