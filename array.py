class Array():
	def __init__(self, size):
		if size <= 50:
			self.__arr = [None] * 50
			self.__sizeOfBuffer = 50

		elif size <= 100 and size > 50:
			self.__arr = [None] * 100
			self.__sizeOfBuffer = 100

		elif size > 100 and size <= 200:
			self.__arr = [None] * 200
			self.__sizeOfBuffer = 200

		elif size > 200 and size <= 400:
			self.__arr = [None] * 400
			self.__sizeOfBuffer = 400

		else:
			self.__arr = [None] * (size * 1.5)
			self.__sizeOfBuffer = len(self.__arr)

		self.size = 0
		self.__firstElement = 0
		self.__lastElement = -1


	def forEach(self, callback):
		for i in range(self.__firstElement, self.__lastElement):
			callback(self.__arr[i])


	def search(self, item):
		for i in range(self.__firstElement, self.__lastElement):
			if self.__arr[i] == item:
				return i

		return -1


	def insert(self, item, index):
		if index > self.__lastElement + 1 or index < 0:
			raise IndexError('Out of range')

		if index == 0 and self.__firstElement != 0:
			self.__firstElement -= 1
			self.__arr[self.__firstElement] = item
			self.size += 1
			return

		elif self.__arr[len(self.__arr) - 1] != None:
			self.__newArray()

		self.size += 1
		self.__lastElement += 1

		temp = [None] * self.__lastElement
		for i in range(self.__firstElement + index, self.__lastElement):
			temp[i] = self.__arr[i]

		for i in range(self.__firstElement + index + 1, self.__lastElement + 1):
			self.__arr[i] = temp[i - 1]
		
		del temp
		self.__arr[self.__firstElement + index] = item


	def delete(self, index):
		if index > self.__lastElement or index < 0:
			raise IndexError('Out of range')

		if index == 0:
			self.size -= 1
			self.__arr[self.__firstElement] = None
			self.__firstElement += 1
			return

		elif index == self.__lastElement:
			self.size -= 1
			self.__arr[self.__lastElement] = None
			self.__lastElement -= 1
			return

		self.size -= 1
		self.__lastElement -= 1
		self.__arr[self.__firstElement + index] = None

		temp = [None] * (self.__lastElement + 2)
		for i in range(self.__firstElement + index, self.__lastElement + 2):	
			temp[i] = self.__arr[i]

		for i in range(self.__firstElement + index - 1, self.__lastElement + 1):
			if temp[i + 1] == None:
				continue

			self.__arr[i] = temp[i + 1]

		del temp
		self.__arr[self.__lastElement + 1] = None


	def append(self, item):
		if self.__lastElement == -1:
			self.__lastElement = 0
			self.__arr[self.__lastElement] = item
			self.size += 1
			return

		elif self.__arr[len(self.__arr) - 1] != None:
			self.__newArray()

		self.__lastElement += 1
		self.size += 1
		self.__arr[self.__lastElement] = item


	def appendStart(self, item):
		if self.__lastElement == -1:
			self.__lastElement = 0
			self.__arr[self.__lastElement] = item
			self.size += 1
			return

		elif self.__firstElement != 0:
			self.__firstElement -= 1
			self.__arr[self.__firstElement] = item
			self.size += 1
			return

		self.insert(item, 0)


	def popStart(self):
		if self.__lastElement == -1:
			raise IndexError("Out of range")

		self.size -= 1
		self.__arr[self.__firstElement] = None
		self.__firstElement += 1

	def pop(self):
		if self.__lastElement == -1:
			raise IndexError("Out of range")

		self.__arr[self.__lastElement] = None
		self.size -= 1
		self.__lastElement -= 1


	def index(self, index):
		if index < self.__firstElement or index > self.__lastElement:
			raise IndexError("Out of range")

		return self.__arr[self.__firstElement + index]

	def replace(self, index, item):
		if index < self.__firstElement or index > self.__lastElement:
			raise IndexError("Out of range")

		self.__arr[index] = item

	
	def arr(self):
		listT = [None] * (self.__lastElement + 1)
		for i in range(self.__firstElement, self.__lastElement + 1):
			listT[i] = self.__arr[i] 

		return listT


	def __newArray(self):
		if self.__sizeOfBuffer >= 400:
			self.__sizeOfBuffer += 100
			self.__arr += [None] * 100

		else:
			self.__arr += [None] * self.__sizeOfBuffer
			self.__sizeOfBuffer *= 2


def filling(arr):
	for i in range(6):
		arr.insert(i + 1, i)


def testInsert():
	arr = Array(6)

	filling(arr)
	arr.insert("a", 6)
	assert arr._Array__arr[6] == "a", "arr._Array__arr[6] should be equal 'a', insert to the end"
	assert arr.size == 7, "arr.size should be equal 7"
	for i in range(arr.size):
		assert arr._Array__arr[i] is not None, f"arr._Array__arr[{i}] should not be equal None"

	arr.insert("b", 2)
	assert arr._Array__arr[2] == "b", "arr._Array__arr[6] should be equal 'b', insert in the middle" 
	assert arr.size == 8, "arr.size should be equal 8"
	for i in range(arr.size):
		assert arr._Array__arr[i] is not None, f"arr._Array__arr[{i}] should not be equal None"

	arr.insert("c", 0)
	assert arr._Array__arr[0] == "c", "arr._Array__arr[0] should be equal 'c', insert to the start"
	assert arr.size == 9, "arr.size should be equal 9" 
	for i in range(arr.size):
		assert arr._Array__arr[i] is not None, f"arr._Array__arr[{i}] should not be equal None"
	#arr.insert("d", 15)

	print("Test (insert) completed")


def testDelete():
	arr = Array(6)

	filling(arr) 
	# 1, 2, 3, 4, 5, 6

	arr.delete(5)
	# 1, 2, 3, 4, 5
	assert arr.size == 5, "arr.size should be equal 5, delete last element" 
	assert arr._Array__arr[5] == None, "arr._Array__arr[5] should be equal None, delete last element" 

	arr.delete(0)
	# 2, 3, 4, 5
	assert arr.size == 4, "arr.size should be equal 4, delete first element"
	assert arr._Array__arr[0] == None, "arr._Array__arr[0] should be equal None, delete first element" 

	arr.delete(1)
	# 2, 4, 5
	assert arr.size == 3, "arr.size should be equal 3, delete middle element"
	assert arr._Array__arr[1] == 2, "arr._Array__arr[1] should be equal 2"
	assert arr._Array__arr[2] == 4, "arr._Array__arr[2] should be equal 4"
	assert arr._Array__arr[3] == 5, "arr._Array__arr[3] should be equal 5"

	print("Test (delete) completed") 


def testSearch():
	arr = Array(6)

	arr.append("a")
	arr.append("b")
	arr.append("c")
	arr.append("d")
	arr.append("f")
	arr.append("g")

	index = arr.search("b")
	assert index == 1, "index should be equal 1"
	assert arr._Array__arr[1] == "b", "arr._Array__arr[1] should be equal 'b'"

	index = arr.search("r")
	assert index == -1, "index should be equal -1, item not found"

	print("Test (search) completed")


def testMisc():
	arr = Array(10)

	filling(arr)
	# 1, 2, 3, 4, 5, 6

	arr.append(7)
	# 1, 2, 3, 4, 5, 6, 7
	assert arr._Array__arr[6] == 7, "arr._Array__arr[6] should be equal 7, append"
	assert arr.size == 7, "arr.size should be equal 7, append"

	arr.pop()
	# 1, 2, 3, 4, 5, 6
	assert arr._Array__arr[5] == 6, "arr._Array__arr[5] should be equal 6, pop"
	assert arr.size == 6, "arr.size should be equal 6, pop"

	item = arr.index(2)
	# 3
	assert item == 3, "item should be equal 3, index"

	arr.replace(2, 10)
	# 1, 2, 10, 4, 5, 6
	assert arr._Array__arr[2] == 10, "arr._Array__arr[2] should be equal 10, replace"
	assert arr.size == 6, "arr.size should be equal 6, replace"

	arr.popStart()
	# 2, 10, 4, 5, 6
	assert arr._Array__arr[1] == 2, "arr._Array__arr[0] should be equal 2, popStart"
	assert arr.size == 5, "arr.size should be equal 5, popStart"

	arr.appendStart(11)
	# 11, 2, 10, 4, 5, 6
	assert arr._Array__arr[0] == 11, "arr._Array__arr[0] should be equal 11, appendStart"

	print("Test (misc) completed")


#testInsert()
#testDelete()
#testSearch()
#testMisc()