arr = [3, 3, 5, 8, 13, 21, 34]

def LinearSearch(num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

num = int(input())
print(LinearSearch(num))