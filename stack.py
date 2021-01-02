class Stack():
	def __init__(self, size):
		self.st = []
		self.size = size

	def pop(self, element):
		self.st.pop(element)

	def push(self, element):
		if len(self.st) > self.size:
			raise IndexError("Out of range")

		else:
			self.st.append(element)

	def isFull(self):
		if len(self.st) == self.size:
			return True

		else:
			return False

	def isEmpty(self):
		if len(self.st) == 0:
			return True

		else:
			return False

	def peek(self):
		return self.st[len(self.st) - 1]


stack = Stack(10)

for i in range(10):
	stack.push(i)

lastItem = stack.peek()
isEmpty = stack.isEmpty()
isFull = stack.isFull()
print(isFull)
print(isEmpty)
print(lastItem)