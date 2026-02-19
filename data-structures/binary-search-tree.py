class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
class BinarySearchTree:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, data):
        NewNode = Node(data)

        if self.head.data == None:
            self.head = NewNode
        else:
            CurrNode = self.head
            while True:
                if NewNode.data > CurrNode.data:
                    if CurrNode.right == None:
                        CurrNode.right = NewNode
                        break
                    else:
                        CurrNode = CurrNode.right
                        continue
                else:
                    if NewNode.data < CurrNode.data:
                        if CurrNode.left == None:
                            CurrNode.left = NewNode
                            break
                        else:
                            CurrNode = CurrNode.left
                            continue
        return print(f"Done adding {data}")

    def search(self, data):
        SearchNode = self.head

        while True:
            if data == SearchNode.data:
                return True
            elif data < SearchNode.data:
                if SearchNode.left == None:
                    return False
                SearchNode = SearchNode.left
            elif data > SearchNode.data:
                if SearchNode.right == None:
                    return False
                SearchNode = SearchNode.right

    def height(self, RootNode):
        if RootNode == None:
            return - 1
        LeftCount = self.height(RootNode.left)
        RightCount = self.height(RootNode.right)

        if LeftCount > RightCount:
            return LeftCount + 1
        else:
            return RightCount + 1
          


Familia = BinarySearchTree()
Familia.insert(100)
Familia.insert(150)
Familia.insert(99)
Familia.insert(45)
Familia.insert(151)
Familia.insert(160)
print(Familia.height(Familia.head))
print(Familia.search(150))
