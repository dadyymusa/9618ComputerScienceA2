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
    if QueueHead < 0 or QueueHead > 20 or QueueHead > QueueTail:
        return False
    else:
        QueueHead = QueueHead + 1
        return QueueData[QueueHead-1]
    
# d



# The subroutine StoreItems() takes ten 7‑character strings as input from the user and
# uses the check digit to validate each input.
#  Each valid input has the check digit removed and is stored in the queue using
# Enqueue().
#  An appropriate message is output if the item is inserted. An appropriate message is
# output if the queue is already full.
#  Invalid inputs are not stored in the queue.
#  The subroutine counts and outputs the number of invalid items that were entered

# multiply the digits in position 0, position 2 and position 4 by 1
# • multiply the digits in position 1, position 3 and position 5 by 3
# • calculate the sum of the products (add together the results from all of the multiplications)
# • divide the sum of the products by 10 and round the result down to the nearest integer to
# get the check digit
# • if the check digit equals 10 then it is replaced with 'X'
def StoreItems():
    count = 0
    for i in range(10):
        val = input(f"{i + 1}:")
        checkDigit = (int(val[0]) + int(val[2]) + int(val[4])) + 3*(int(val[1]) + int(val[3]) + int(val[5]))
        checkDigit = checkDigit // 10
        if (checkDigit == 10 and val[6] == 'X') or checkDigit == int(val[6]):
            flag = Enqueue(val[:6])
            if flag == True:
                print('Inserted')
            
        else:
            print('Not Inserted')
            count += 1
        
    print("Invalid items:", count)

StoreItems()

