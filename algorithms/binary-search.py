arr = [3, 3, 5, 8, 13, 21, 34]

def BinarySearch(num):
    hi = len(arr) - 1
    lo = 0

    while lo <= hi:
        mid = hi + lo // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

num = int(input())
ans = BinarySearch(num)
print(ans)