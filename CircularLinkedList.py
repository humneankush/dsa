class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setNext(self, next_node):
        self.next = next_node

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def hasNext(self):
        return self.getNext() is not None

    def __repr__(self):
        return repr(self.data)

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.getNext()
            if current == self.head:
                break
        print("...")

    # def __repr__(self):
    #     nodes = []
    #     curr = self.head
    #     while curr:
    #         nodes.append(repr(curr))
    #         curr = curr.next
    #     return "[" + ", ".join(nodes) + "]"

    def insertAtBeginning(self, data):
        new_node = Node()
        new_node.setData(data)
        new_node.setNext(new_node)  # Circular link to itself

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.getNext() != self.head:
                current_node = current_node.getNext()
            current_node.setNext(new_node)
            new_node.setNext(self.head)
            self.head = new_node

        
        




circular_linked_list = CircularLinkedList()

circular_linked_list.insertAtBeginning(1)
circular_linked_list.insertAtBeginning(2)

circular_linked_list.display()
