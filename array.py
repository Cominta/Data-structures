import copy

class Array():
	def __init__(self, size):
		self.arr = []
		self.size = size

		for i in range(self.size):
			self.arr.append(None)


	#def __setattr__(self, attr, value):
	#	if attr == "size":
	#		raise AttributeError


	def forEach(self, callback):
		for i in range(len(self.arr)):
			callback(self.arr[i])


	def search(self, item):
		for i in range(len(self.arr)):
			if self.arr[i] == item:
				return i


	def insert(self, item, index):
		oldArr = copy.copy(self.arr)
		del self.arr
		self.arr = []
		self.size += 1

		for i in range(self.size):
			self.arr.append(None)

		for i in range(0, index):
			self.arr[i] = oldArr[i]

		self.arr[index] = item

		for i in range(index + 1, len(oldArr)):
			self.arr[i] = oldArr[i]


arr = Array(10)

def printEach(item):
	print(item)

print(arr.arr)
arr.insert("y", 1)
print(arr.arr)
arr.insert("w", 5)
print(arr.arr)