class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return 

        currNode = self.head

        while currNode.next != None:
            currNode = currNode.next

        currNode.next = newNode

    def delete(self, value):
        
        if self.head is None: 
            return "List is empty"
        
        if self.head.data == value:
            self.head = self.head.next
            return

        currNode = self.head
        prevNode = None 

        while currNode is not None and currNode.data != value:
            prevNode = currNode
            currNode = currNode.next
        
        if currNode is None:
            print('Value not found')
            return

        prevNode.next = currNode.next

arr = [[-1, 0, -1] * 2] * 9
print(arr)


def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = value
    return arr

def recursive_insertion_sort(arr, n=None):
    # If n is not provided, start with the full length of the array
    if n is None:
        n = len(arr)
        
    # 1. BASE CASE: An array of 1 element is already sorted.
    if n <= 1:
        return arr

    # 2. RECURSIVE STEP: Sort the first n-1 elements first
    recursive_insertion_sort(arr, n - 1)

    # 3. INSERTION LOGIC: Insert the last element (at index n-1) into its sorted place
    key = arr[n - 1]
    j = n - 2

    # Shift elements to the right to make room for the key
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # Drop the key into its correct position
    arr[j + 1] = key

    return arr

def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop tracks how many elements have been placed at the end
    for i in range(n):
        # Inner loop compares adjacent elements up to the unsorted boundary
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr


def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap happened!
                
        # If no two elements were swapped by the inner loop, then break
        if not swapped:
            break
            
    return arr

QueueArr = [-1] * 9

head = -1
tail = -1

def Enqueue(data):
    global head, tail, QueueArr
    if tail == -1:
        head += 1
        QueueArr[head] = data
        tail += 1
    elif tail < n  - 1:
        tail += 1
        QueueArr[tail] = data
    else:
        return False

def Dequeue(data):
    global head, tail, QueueArr
    if head == - 1:
        return False
    else:
        value = QueueArr[head]
        head += 1

