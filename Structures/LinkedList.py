class Node():
	def __init__(self, item):
		self.item = item
		self.nextNode = None


class LinkedList():
	def __init__(self):
		self.head = None
		self.__count = 0


	def insertToTheEnd(self, item):
		self.__checkLoop(self.__count)
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
		if self.head != None:
			tempCount = self.__count / 2
			self.__checkLoop(int(tempCount))
			newNode = Node(item)
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
		newNode = Node(item)

		if node:
			result = self.search(itemAfter)
			if result == None:
				raise AttributeError("Item not found")

			#self.__checkLoop(result[1])
			newNode.nextNode = result[0].nextNode
			result[0].nextNode = newNode

		else:
			raise IndexError("List is empty")


	def insertBeforeItem(self, item, itemBefore):
		node = self.head
		if node:
			result = self.search(itemBefore)
			if result == None:
				raise AttributeError("Item not found")

			newNode = Node(item)

			if node.item == itemBefore:
				newNode.nextNode = node
				self.head = newNode
				return

			for i in range(result[1] - 1):
				node = node.nextNode

			newNode.nextNode = node.nextNode
			node.nextNode = newNode

		else:
			raise IndexError("List is empty")


	def deleteFirstElement(self):
		node = self.head
		if node:
			self.__checkLoop()
			self.head = node.nextNode
			self.__count -= 1

		else:
			raise IndexError("List is empty")


	def deleteLastElement(self):
		node = self.head
		if node:
			self.__checkLoop(self.__count)
			for i in range(self.__count - 2):
				node = node.nextNode

			node.nextNode = None
			self.__count -= 1 

		else:
			raise IndexError("List is empty")


	def deleteCentralElement(self):
		node = self.head
		if node:
			tempCount = self.__count / 2
			self.__checkLoop(int(tempCount))
			for i in range(int(tempCount) - 2):
				node = node.nextNode

			node.nextNode = node.nextNode.nextNode
			self.__count -= 1 

		else:
			raise IndexError("List is empty")


	def search(self, item):
		if self.head:
			node = self.head
			tempList = [None] * (self.__count - 1)

			if node.nextNode == node:
				raise IndexError("List is wrong")

			elif node.item == item:
				return (node, 0)

			for i in range(self.__count - 1):
				tempList[i] = node
				node = node.nextNode
				if node.item == item:
					return (node, i + 1)

				for j in range(len(tempList)):
					if tempList[j] == node:
						raise IndexError("List is wrong") 

			return None

		else:
			raise IndexError("List is empty")


	def forEach(self, callback):
		if self.head:
			node = self.head
			while node:
				callback(node)
				node = node.nextNode

		else:
			raise IndexError("List is empty")


	def index(self, index):
		if self.head:
			node = self.head

			if index > self.__count:
				raise IndexError("Out of range")

			for i in range(index):
				node = node.nextNode

			return node

		else:
			raise IndexError("List is empty")


	def __checkLoop(self, index = 0):
		node = self.head
		if node == None:
			return

		elif node.nextNode == None:
			return

		i = 0
		if index == 0:
			index += 1

		tempList = [None] * index
		while i != index:
			tempList[i] = node
			node = node.nextNode
			for j in range(len(tempList)):
				if tempList[j] == node:
					raise IndexError("List is wrong")

			i += 1


	def printList(self):
		node = self.head

		while node:
			print(node.item)
			node = node.nextNode