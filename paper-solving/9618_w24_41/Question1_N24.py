# qp - https://bestexamhelp.com/exam/cambridge-international-a-level/computer-science-9618/2024/9618_w24_qp_41.pdf
# ms - https://bestexamhelp.com/exam/cambridge-international-a-level/computer-science-9618/2024/9618_w24_ms_41.pdf

# Question1_N24
#  1a
def ReadData():
    try:
        Colors = []
        File = open('./9618_w24_41/Data.txt')
        Colors = File.read().split("\n")
        File.close()   
        return Colors
    except:
        print("File Not Found")


# 1bi 

def FormatArray(arr):
    string = ""
    for i in range(len(arr)):
        string = string + " " + arr[i]
    return string[1::]

# 1bii

arr = ReadData()
print(arr)

# 1c
# takes two strings as parameters
# • compares each string, one character at a time, to identify which string comes first
# alphabetically. If the first two characters are the same, the second character of each
# string is compared. This continues until the two characters are different.

def CompareStrings(one, two):
    i = 0
    while ord(one[i]) == ord(two[i]):
        i += 1

    if ord(one[i]) < ord(two[i]):
        return 1
    else:
        return 2  
    
# 1d
# The function Bubble() takes an array of strings as a parameter and sorts the data into
# ascending alphabetical order, using a bubble sort. The bubble sort uses CompareStrings()
# to compare each string.

def Bubble(lst):
    for i in range(len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            compare = CompareStrings(lst[j], lst[j + 1])
            if compare == 2:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


Bubble(arr)

print(FormatArray(arr))
