class Node:
	def __init__(self):
		self.data = None
		self.next = None

	def setNext(self,next):
		self.next = next

	def getNext(self):
		return self.next

	def setData(self,data):
		self.data = data

	def getData(self):
		return self.data

	def hasNext(self)
		return self.getNext() != None


class LinkedList:
	def __init__(self):
		self.head = None
		self.length = 0

	def insertAtBeginning(self,data):
		newNode = Node()
		newNode.setData(data)

		if self.length == o:
			self.head = newNode
		else :
			newNode.setNext(self.head)
			self.head = newNode
		self.length += 1

	def listLength(self):
		current_node = self.head
		count = 0
		while current_node is not None:
			count = count + 1
			current_node = current_node.getNext()
		return count



