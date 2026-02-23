# Question 3

# (a) The main program initialises all the elements in QueueData to a suitable null value,
# QueueHead to −1 and QueueTail to −1.

QueueData = [""] * 20
QueueHead = -1
QueueTail = -1


# (b) The function Enqueue() takes the data to insert into the queue as a parameter.
#  If the queue is not full, it inserts the parameter in the queue, updates the appropriate pointer(s)
# and returns TRUE. If the queue is full, it returns FALSE.
def Enqueue(data):
    global QueueData
    global QueueHead
    global QueueTail

    if QueueTail == 19:
        return False
    elif QueueHead == -1:
        QueueHead = 0
    QueueData.append(data)
    QueueTail += 1
    return True

def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail
    if QueueHead < 0 or QueueHead > 20:
        return False
    else:
        QueueHead = QueueHead + 1
        return QueueData[QueueHead-1]