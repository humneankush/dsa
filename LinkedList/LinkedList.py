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


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return "[" + ", ".join(nodes) + "]"

    def insertAtBeginning(self, data):
        new_node = Node()
        new_node.setData(data)

        if self.length == 0:
            self.head = new_node
        else:
            new_node.setNext(self.head)
            self.head = new_node
        self.length += 1

    def insertAtEnd(self, data):
        new_node = Node()
        new_node.setData(data)

        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.getNext() is not None:
                current_node = current_node.getNext()
            current_node.setNext(new_node)
        self.length += 1

    def insertAtPosition(self, data, position):
        if position <= 0:
            self.insertAtBeginning(data)
        elif position >= self.length:
            self.insertAtEnd(data)
        else:
            new_node = Node()
            new_node.setData(data)
            count = 0
            current_node = self.head
            while count < position - 1:
                count += 1
                current_node = current_node.getNext()
            new_node.setNext(current_node.getNext())
            current_node.setNext(new_node)
        self.length += 1

    def deleteFromBeginingInLinkedList(self):
        if self.head is None:
            return "List is empty"        
        self.head = self.head.getNext()
        self.length -= 1

  
    def deleterFromEndInLinkedList(self):
        if self.head is None:
            return
        if self.head.getNext() is None:
            self.head.setNext(None)
            self.length = 0
            return 
        
        prev_node = None
        current_node = self.head

        while current_node.getNext() is not None:
            prev_node = current_node
            current_node = current_node.getNext()
        if prev_node is not None:
            prev_node.setNext(None)
        self.length -= 1


    def middleOfLinkedList(self):
        if self.head is None:
            return "list is empty"
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None:
            fast_ptr = fast_ptr.getNext()
            if fast_ptr is None:
                return slow_ptr
            fast_ptr = fast_ptr.getNext()
            slow_ptr = slow_ptr.getNext()
            return slow_ptr

    def listLength(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.getNext()
        return count
    
    def reveseLinkedList(self):
        dummy_node = None
        current_node = self.head
        
        while current_node is not None:
            nextNode = current_node.getNext()
            current_node.setNext(dummy_node)
            dummy_node = current_node
            current_node = nextNode
        self.head = dummy_node


linked_list = LinkedList()
linked_list.insertAtBeginning(1)
linked_list.insertAtBeginning(2)
linked_list.insertAtBeginning(3)
linked_list.insertAtEnd(3)



print(linked_list)
linked_list.reveseLinkedList()  # Output: [3, 2, 1, 3]
print(linked_list)

linked_list.deleteFromBeginingInLinkedList()
print(linked_list)
linked_list.deleteFromBeginingInLinkedList()
print(linked_list)

linked_list.deleterFromEndInLinkedList()
print(linked_list)

linked_list.deleterFromEndInLinkedList()
print(linked_list)




