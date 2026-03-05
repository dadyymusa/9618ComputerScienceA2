arr = [9, 19, 23, 45, 65, 78]

def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for n in range(len(arr) - i - 1):
            if arr[n] > arr[n + 1]:
                temp = arr[n]
                arr[n] = arr[n + 1]
                arr[n + 1] = temp
    return arr

BubbleSort(arr)

print(arr)