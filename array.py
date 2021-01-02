class Array():
	def __init__(self, size):
		self.arr = []
		self.size = size

		for i in range(self.size):
			self.arr.append(None)

	def forEach(self, callback):
		for i in range(len(self.arr)):
			callback(self.arr[i])

	def search(self, item):
		for i in range(len(self.arr)):
			if self.arr[i] == item:
				return i

	def insert(self, item, index):
		if index > self.size:
			raise IndexError(f"Index out of range")

		self.arr[index] = item

arr = Array(5)

def printEach(item):
	print(item)

arr.insert(0, 0)
arr.insert(1, 2)
arr.insert(2, 1)
arr.forEach(printEach)
search = arr.search(0)
print(search)