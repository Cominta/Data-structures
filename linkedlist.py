class Node():
	def __init__(self, item):
		self.item = item
		self.nextNode = None


class LinkedList():
	def __init__(self):
		self.head = None
		self.__count = 0


	def insertToTheEnd(self, item):
		self.__checkLoop()
		node = self.head
		newNode = Node(item)
		self.__count += 1

		if node:
			while node.nextNode:
				node = node.nextNode

			node.nextNode = newNode

		else:
			self.head = newNode


	def insertToTheStart(self, item):
		self.__checkLoop()
		newNode = Node(item)
		node = self.head
		newNode.nextNode = node
		self.head = newNode
		self.__count += 1


	def insertToTheMiddle(self, item):
		self.__checkLoop()
		if self.head != None:
			newNode = Node(item)
			tempCount = self.__count / 2
			node = self.head
			for i in range(int(tempCount) - 1):
				node = node.nextNode

			newNode.nextNode = node.nextNode
			node.nextNode = newNode
			self.__count += 1

		else:
			raise IndexError("List is empty")


	def insertAfterItem(self, item, itemAfter):
		node = self.head
		self.__checkLoop()
		newNode = Node(item)

		if node:
			for i in range(self.__count):
				if node.item == itemAfter:
					newNode.nextNode = node.nextNode
					node.nextNode = newNode
					break

				node = node.nextNode

		else:
			raise IndexError("List is empty")


	def insertBeforeItem(self, item, itemBefore):
		node = self.head
		self.__checkLoop()
		if node:
			newNode = Node(item)

			if node.item == itemBefore:
				newNode.nextNode = node
				self.head = newNode
				return

			for i in range(self.__count):
				if node.nextNode.item == itemBefore:
					newNode.nextNode = node.nextNode
					node.nextNode = newNode
					break

				node = node.nextNode

		else:
			raise IndexError("List is empty")


	def deleteFirstElement(self):
		node = self.head
		self.__checkLoop()
		if node:
			self.head = node.nextNode
			self.__count -= 1

		else:
			raise IndexError("List is empty")


	def deleteLastElement(self):
		node = self.head
		self.__checkLoop()
		if node:
			for i in range(self.__count - 2):
				node = node.nextNode

			node.nextNode = None
			self.__count -= 1 

		else:
			raise IndexError("List is empty")


	def deleteCentralElement(self):
		node = self.head
		self.__checkLoop()
		if node:
			tempCount = self.__count / 2
			for i in range(int(tempCount) - 2):
				node = node.nextNode

			node.nextNode = node.nextNode.nextNode
			self.__count -= 1 

		else:
			raise IndexError("List is empty")


	def search(self, item):
		node = self.head
		self.__checkLoop()

		while node:
			if node.item == item:
				return node

			node = node.nextNode

		return None


	def forEach(self, callback):
		self.__checkLoop()
		node = self.head
		while node:
			callback(node.item)
			node = node.nextNode


	def index(self, index):
		node = self.head
		self.__checkLoop()

		if index > self.__count:
			raise IndexError("Out of range")

		if node:
			for i in range(index):
				node = node.nextNode

			return node

		else:
			raise IndexError("List is empty")


	def __checkLoop(self):
		node = self.head
		tempList = []

		while node:
			if node in tempList:
				raise IndexError("List is wrong")

			tempList.append(node)
			node = node.nextNode

		return


	def printList(self):
		node = self.head

		while node:
			print(node.item)
			node = node.nextNode


def testInsert():
	linkedlist = LinkedList()

	linkedlist.insertToTheStart(0)
	# 0
	assert linkedlist.head.item == 0, "linkedlist.head.item should be equal 0, Insert to the start" 

	linkedlist.insertToTheEnd(1)
	# 0, 1
	node = linkedlist.head
	while node.nextNode:
		node = node.nextNode

	assert node.item == 1, "last node.item should be equal 1, Insert to the end"

	linkedlist.insertToTheMiddle(2)	
	# 0, 2, 1
	node = linkedlist.head
	secondNode = node.nextNode
	assert secondNode.item == 2, "node.item in the middle should be equal 2, Insert to the middle"

	linkedlist.insertAfterItem(7, 0)
	# 0, 7, 2, 1
	assert linkedlist.head.nextNode.item == 7, "second node.item should be equal 7, insert after item"

	linkedlist.insertBeforeItem(6, 7)
	# 0, 6, 7, 2, 1
	assert linkedlist.head.nextNode.item == 6, "second node.item should be equal 6, insert before item"

	print("Test (insert) completed")


def testDelete():
	linkedlist = LinkedList()

	linkedlist.insertToTheStart(0)
	linkedlist.insertToTheEnd(1)
	linkedlist.insertToTheEnd(2)
	linkedlist.insertToTheEnd(3)
	linkedlist.insertToTheMiddle(10)
	# 0, 1, 10, 2, 3

	linkedlist.deleteFirstElement()
	# 1, 10, 2, 3
	assert linkedlist.head.item == 1, "first node.item should be equal 1, delete first element"

	linkedlist.deleteLastElement()
	# 1, 10, 2
	node = linkedlist.head
	while node.nextNode:
		node = node.nextNode

	assert node.item == 2, "last node.item should be equal 2, delete last element"

	linkedlist.deleteCentralElement()
	# 1, 2
	node = linkedlist.head
	assert node.item == 1, "first element should be equal 1, delete central element"
	assert node.nextNode.item == 2, "last element should be equal 2, delete central element"

	print("Test (delete) completed")


def testSearch():
	linkedlist = LinkedList()

	linkedlist.insertToTheEnd(0)
	linkedlist.insertToTheEnd(1)
	linkedlist.insertToTheEnd(2)
	linkedlist.insertToTheStart(10)
	linkedlist.insertToTheMiddle(9)
	# 10, 0, 9, 1, 2

	nodeWithItem = linkedlist.search(9)
	assert nodeWithItem.item == 9, "nodeWithItem.item should be equal 9"

	nodeWithItem = linkedlist.search(10)
	assert nodeWithItem.item == 10, "nodeWithItem.item should be equal 10"

	nodeWithItem = linkedlist.search(2)
	assert nodeWithItem.item == 2, "nodeWithItem.item should be equal 2"

	nodeWithItem = linkedlist.search(50)
	assert nodeWithItem == None, "nodeWithItem should be equal None, item not found" 

	print("Test (search) completed")


def testIndex():
	linkedlist = LinkedList()

	linkedlist.insertToTheEnd(0) # 0
	linkedlist.insertToTheStart(1) # 1, 0
	linkedlist.insertToTheMiddle(2) # 1, 2, 0
	linkedlist.insertBeforeItem(3, 0) # 1, 2, 3, 0
	linkedlist.insertToTheEnd(4) # 1, 2, 3, 0, 4
	linkedlist.insertToTheEnd(5) # 1, 2, 3, 0, 4, 5

	index = linkedlist.index(2)
	# 3
	assert index.item == 3, "index.item should be equal 3, index 2"

	index = linkedlist.index(5)
	# 5
	assert index.item == 5, "index.item should be equal 5, index 5"

	print("Test (index) completed")


testInsert()
testDelete()
testSearch()
testIndex()