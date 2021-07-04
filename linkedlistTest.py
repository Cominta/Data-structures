from Structures.LinkedList import LinkedList

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
	assert nodeWithItem[0].item == 9, "nodeWithItem[0].item should be equal 9"
	assert nodeWithItem[1] == 2, "nodeWithItem[1] should be equal 4 "

	nodeWithItem = linkedlist.search(10)
	assert nodeWithItem[0].item == 10, "nodeWithItem.item should be equal 10"
	assert nodeWithItem[1] == 0, "nodeWithItem[1] should be equal 0"

	nodeWithItem = linkedlist.search(2)
	assert nodeWithItem[0].item == 2, "nodeWithItem[0].item should be equal 2"
	assert nodeWithItem[1] == 4, "nodeWithItem[1] should be equal 4"

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


def testLoop():
	linkedlist = LinkedList()

	linkedlist.insertToTheEnd(0)
	linkedlist.insertToTheStart(1)
	linkedlist.insertToTheMiddle(2)
	linkedlist.insertAfterItem(3, 1)
	linkedlist.insertBeforeItem(4, 1)
	# 4, 1, 3, 2, 0

	try:
		node = linkedlist.head
		node.nextNode = node
		linkedlist.insertToTheEnd(5)
		linkedlist.insertAfterItem(5, 2)
		raise AssertionError("linkedlist.insertToTheEnd have to call except")

	except IndexError:
		pass

	try:
		node = linkedlist.head
		node.nextNode.nextNode.nextNode.nextNode.nextNode = node.nextNode
		linkedlist.insertToTheEnd(5)
		linkedlist.insertAfterItem(5, 2)
		raise AssertionError("linkedlist.insertToTheEnd have to call except")

	except IndexError:
		pass
		
	print("Test (loop) completed")


testInsert()
testDelete()
testSearch()
testIndex()
testLoop()