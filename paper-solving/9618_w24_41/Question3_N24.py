# 3a
LinkedList = []

for i in range(20):
    LinkedList.append([-1, i + 1])
    if i == 19:
        LinkedList[i][1] = -1

FirstEmpty = 0 #index of the first element
FirstNode = -1 # index of the first node in LinkedList

# 3b
# The procedure InsertData() takes five positive integers as input from the user and inserts
# these into the linked list.
#  Each data item is inserted at the front of the linked list

def InsertData():
    global FirstEmpty, FirstNode
    for i in range(5):
        data = int(input(f"{i + 1} -> "))
        if FirstEmpty != -1:
            NextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = data
            LinkedList[FirstEmpty][1] = FirstEmpty - 1
            FirstNode = FirstEmpty
            FirstEmpty = NextEmpty

# ci
# The procedure OutputLinkedList() outputs the data in the linked list in order by following
# the pointers from FirstNode.

def OutputLinkedList():
    global FirstNode
    for i in range(FirstNode, -1, -1):
        print(LinkedList[i][0])

# cii
# 5 1 2 3 8 -> insert this 
InsertData()
OutputLinkedList()
print(LinkedList)
# d
# The procedure RemoveData() removes a node from the linked list.
#  The procedure takes the data item to be removed from the linked list as a parameter.
#  The procedure checks each node in the linked list, starting with the node FirstNode, until it
# finds the node to be removed. This node is added to the empty list, and pointers are changed
# as appropriate. The procedure only removes the first occurrence of the parameter.
def RemoveData(val):
    global FirstEmpty, FirstNode, LinkedList
    if LinkedList[FirstNode][0] == val:
        LinkedList[FirstNode][0] = -1
        pointer = LinkedList[FirstNode][1] #storing the index of the next node
        LinkedList[FirstNode][1] = FirstEmpty
        FirstEmpty = FirstNode
        FirstNode = pointer
        return
    else:
         CurrentNode = FirstNode
         while True:
             NextNode = LinkedList[CurrentNode][1]
             if LinkedList[NextNode][0] == val:
                 LinkedList[CurrentNode][1] = LinkedList[NextNode][1]
                 LinkedList[NextNode][0] = -1
                 LinkedList[NextNode][1]  = FirstEmpty
                 FirstEmpty = NextNode
                 return
             else:
                 CurrentNode = LinkedList[CurrentNode][1]

RemoveData(7)
OutputLinkedList()
print(LinkedList)