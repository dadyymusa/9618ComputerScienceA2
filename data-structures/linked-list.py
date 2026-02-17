# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return

        currNode = self.head
        while currNode.next is not None:
            currNode = currNode.next

        currNode.next = newNode


    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found")
            return

        temp.next = temp.next.next


    def search(self, value):
        temp = self.head
        position = 1

        while temp:
            if temp.data == value:
                print(f"Value found at position {position}")
                return
            temp = temp.next
            position += 1

        print("Value not found")


    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# creating a linked list
Animals = LinkedList()

# inserting nodes
Animals.insert("Human")
Animals.insert("Cow")
Animals.insert("Cat")

# traversing
Animals.traverse()


# searching for a node
Animals.search("Meow")
Animals.search("cats")
# deleting a node
Animals.delete("Human")
Animals.traverse()