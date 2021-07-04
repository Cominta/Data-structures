import array
from Structures.Array import Array

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

	arr.setIndex(2, 10)
	# 1, 2, 10, 4, 5, 6
	assert arr._Array__arr[2] == 10, "arr._Array__arr[2] should be equal 10, setIndex"
	assert arr.size == 6, "arr.size should be equal 6, setIndex"

	arr.popStart()
	# 2, 10, 4, 5, 6
	assert arr._Array__arr[1] == 2, "arr._Array__arr[0] should be equal 2, popStart"
	assert arr.size == 5, "arr.size should be equal 5, popStart"

	arr.appendStart(11)
	# 11, 2, 10, 4, 5, 6
	assert arr._Array__arr[0] == 11, "arr._Array__arr[0] should be equal 11, appendStart"

	print("Test (misc) completed")


def testMemory():
	#Memory leak (right side)
	arr = Array(150)

	filling(arr)

	for i in range(100):
		arr.append(i + 1)
	
	for i in range(20):
		arr.pop()

	assert arr._Array__sizeOfBuffer == 100, "arr._Array__sizeOfBuffer should be equal 100, memory lick (right side)"
	assert arr.index(85) == 80, "arr.index(85) should be equal 86, memory lick (right side)"

	#New array
	arr = Array(10)

	for i in range(200):
		arr.append(i + 1)
	
	arr.insert(1000, 0)

	assert arr.index(0) == 1000, "arr.index(0) should be equal 1000, new array"
	assert arr._Array__sizeOfBuffer == 250, "arr._Array_sizeOfBuffer should be equal 250, new array"

	for i in range(1, 201):
		assert arr._Array__arr[i] == i, f"arr._Array__arr[{i}] = {arr._Array__arr[i]}, i = {i}"

	assert arr._Array__firstElement == 0, "arr._Array__firstElement should be equal 0, new array"
	assert arr._Array__lastElement == 200, "arr._Array__firstElement should be equal 149, new array"

	#Memory leak (left side)
	arr = Array(200)

	for i in range(200):
		arr.append(i + 1)

	for i in range(120):
		arr.popStart()

	assert arr._Array__firstElement == 20, "arr._Array__firstElement should be equal 19"
	assert arr._Array__sizeOfBuffer == 100, "arr._Array__sifeOfBuffer should be equal 100"

	print("Test (memory) completed")


testInsert()
testDelete()
testSearch()
testMisc()
testMemory()