class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue = self.queue[1:]

    def showqueue(self):
        for n in self.queue:
            print(n)
        print()


Line = Queue()
Line.insert('Musa')
Line.insert('Sudad')
Line.showqueue()
Line.dequeue()
Line.showqueue()

