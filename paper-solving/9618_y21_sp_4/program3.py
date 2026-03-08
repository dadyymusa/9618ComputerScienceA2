#  a
QueueData = [''] * 20
Head = -1
Tail = -1
# b
# if the element was successfully added to the queue, the function should return TRUE
# • if the queue was full and the item could not be added to the queue the function should
# returns FALSE
# • each time an item is successfully added, the function should updates the pointers
def Enqueue(val):
    global Head, Tail, QueueData
    if Tail == 19:
        return False
    elif Head == -1:
        QueueData[0] = val
        Head += 1
        Tail += 1
        return True
    elif Tail < 19:
        Tail += 1
        QueueData[Tail]  = val
            
print(QueueData)
Enqueue(5)
print(QueueData)

# c
# • asks the user to input a filename
# • reads the data from the text file into QueueData.
# The function returns the following values when:
# • all of the data is successfully read into the queue, the function returns the value 2
# • the queue is full and not all the data could be inserted into the queue, the function returns
# the value 1
# • the text file could not be found, the function returns the value –1.
