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
			self.__arr = [None] * (size + 100)
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
		if index > self.__lastElement + 1 - self.__firstElement or index < 0:
			raise IndexError('Out of range')

		if index == 0 and self.__firstElement != 0:
			self.__firstElement -= 1
			self.__arr[self.__firstElement] = item
			self.size += 1
			return

		elif len(self.__arr) - 1 == self.__lastElement:
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
		if index > self.__lastElement - self.__firstElement or index < 0:
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

		elif self.__sizeOfBuffer > 100 and 0 - self.__firstElement < -100:
			self.__memoryLeak("left")

		elif self.__sizeOfBuffer > 100 and self.__sizeOfBuffer - self.__lastElement > 100:
			self.__memoryLeak("right")

		self.size -= 1
		self.__lastElement -= 1
		self.__arr[self.__firstElement + index] = None

		temp = [None] * (self.__lastElement + 2)
		for i in range(self.__firstElement + index, self.__lastElement + 2):	
			temp[i] = self.__arr[i]

		for i in range(self.__firstElement + index - 1, self.__lastElement + 1):
			if i + 1 == self.__firstElement + index:
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

		if self.__sizeOfBuffer - 1 == self.__lastElement:
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

		if self.__sizeOfBuffer > 100 and 0 - self.__firstElement < -100:
			self.__memoryLeak("left")

	def pop(self):
		if self.__lastElement == -1:
			raise IndexError("Out of range")
		
		self.__arr[self.__lastElement] = None
		self.size -= 1
		self.__lastElement -= 1

		if self.__sizeOfBuffer > 100 and self.__sizeOfBuffer - self.__lastElement > 100:
			self.__memoryLeak("right")


	def index(self, index):
		if index < self.__firstElement or index > self.__lastElement - self.__firstElement:
			raise IndexError("Out of range")

		return self.__arr[self.__firstElement + index]

	def setIndex(self, index, item):
		if index < self.__firstElement or index > self.__lastElement - self.__firstElement:
			raise IndexError("Out of range")

		self.__arr[self.__firstElement + index] = item

	
	def arr(self):
		listT = [None] * (self.__lastElement + 1)
		for i in range(self.__firstElement, self.__lastElement + 1):
			listT[i] = self.__arr[i] 

		return listT


	def __newArray(self):
		self.__sizeOfBuffer += 100
		self.__arr += [None] * 100


	def __memoryLeak(self, side):
		if side == "right":
			i = self.__sizeOfBuffer - 100
			while self.__sizeOfBuffer != i:
				self.__sizeOfBuffer -= 1
				del self.__arr[i]
		
		elif side == "left":
			for i in range(100):
				del self.__arr[0]

			self.__firstElement -= 100
			self.__sizeOfBuffer -= 100