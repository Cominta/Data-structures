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

		return -1


	def insert(self, item, index):
		if index > self.size and index < 0:
			raise IndexError('Out of range')

		self.size += 1

		arrTemp = self.create_array(self.size)

		for i in range(index):
			arrTemp[i] = self.arr[i]

		for j in range(index, self.size):
			arrTemp[j] = self.arr[j - 1]

		arrTemp[index] = item

		del self.arr
		self.arr = arrTemp


	def delete(self, index):
		if index > self.size and index < 0:
			raise IndexError('Out of range')

		self.size -= 1

		arrTemp = self.create_array(self.size)
		for i in range(index):
			arrTemp[i] = self.arr[i]

		for j in range(index, self.size):
			arrTemp[j] = self.arr[j + 1]

		del self.arr
		self.arr = arrTemp


	def create_array(self, size):
		arr = [None] * size
		return arr


def filling(arr):
	for i in range(6):
		arr.arr[i] = i + 1


def test_array_insert():
	arr = Array(6)

	filling(arr)

	arr.insert("a", 6)
	assert arr.arr[6] == "a", "arr.arr[6] should be equal 'a', Insert to the end"
	assert arr.size == 7, "arr.size should be equal 7"
	for i in range(arr.size):
		assert arr.arr[i] is not None, f"arr.arr[{i}] should not be equal None"

	arr.insert("b", 5)
	assert arr.arr[5] == "b", "arr.arr[6] should be equal 'b', Insert in the middle" 
	assert arr.size == 8, "arr.size should be equal 8"
	for i in range(arr.size):
		assert arr.arr[i] is not None, f"arr.arr[{i}] should not be equal None"

	arr.insert("c", 0)
	assert arr.arr[0] == "c", "arr.arr[6] should be equal 'c', Insert to the start"
	assert arr.size == 9, "arr.size should be equal 9" 
	for i in range(arr.size):
		assert arr.arr[i] is not None, f"arr.arr[{i}] should not be equal None"
	#arr.insert("d", 15)

	print("Test (insert) completed")


def test_array_delete():
	arr = Array(6)

	filling(arr) 
	# 1, 2, 3, 4, 5, 6

	arr.delete(5)
	# 1, 2, 3, 4, 5
	assert arr.size == 5, "arr.size should be equal 5, Delete last element" 
	for i in range(arr.size):
		assert arr.arr[i] == i + 1, f"arr.arr[{i}] should be equal {i + 1}"

	arr.delete(0)
	# 2, 3, 4, 5
	assert arr.size == 4, "arr.size should be equal 4, Delete first element"
	for i in range(arr.size):
		assert arr.arr[i] == i + 2, f"arr.arr[{i + 1}] should be equal {i + 1}" 

	arr.delete(1)
	# 2, 4, 5
	assert arr.size == 3, "arr.size should be equal 3, Delete middle element"
	assert arr.arr[0] == 2, "arr.arr[0] should be equal 2"
	assert arr.arr[1] == 4, "arr.arr[1] should be equal 4"
	assert arr.arr[2] == 5, "arr.arr[2] should be equal 5"

	print("Test (delete) completed") 


def test_array_search():
	arr = Array(6)

	arr.arr[0] = "a"
	arr.arr[1] = "b"
	arr.arr[2] = "c"
	arr.arr[3] = "d"
	arr.arr[4] = "f"
	arr.arr[5] = "g"

	index = arr.search("b")
	assert index == 1, "index should be equal 1"
	assert arr.arr[1] == "b", "arr.arr should be equal 'b'"

	index = arr.search("r")
	assert index == -1, "index should be equal -1, item not found"

	print("Test (search) completed")


#test_array_insert()
#test_array_delete()
#test_array_search()