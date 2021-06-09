import math
import copy

class Heap():
    def __init__(self, root):
        self.__heap = [root]
        self.count = 1

    
    def add(self, value):
        self.__heap += [value]
        self.count += 1
        self.__checkPriorityParents(len(self.__heap) - 1)


    def pop(self):
        if self.count == 1:
            raise IndexError("heap is empty")

        tempHeap = [None] * (len(self.__heap) - 1)
        self.count -= 1

        for i in range(len(self.__heap) - 1):
            tempHeap[i] = self.__heap[i]

        tempHeap[0] = self.__heap[len(self.__heap) - 1]
        self.__heap = copy.copy(tempHeap)

        if self.count == 2 and self.__heap[0] < self.__heap[1]:
            self.__heap[0], self.__heap[1] = self.__heap[1], self.__heap[0]
            return

        self.__checkPriorityChildren(0)


    def search(self, element):
        for i in range(self.count):
            if self.__heap[i] == element:
                return i
        
        return None


    def index(self, index):
        if index > self.count - 1:
            return None

        return self.__heap[index]

    
    def heap(self):
        # for security
        tempHeap = copy.copy(self.__heap)
        return tempHeap


    def __checkPriorityChildren(self, index):
        while index * 2 + 1 < len(self.__heap) - 1:
            if self.__heap[index * 2 + 1] > self.__heap[index * 2 + 2]:
                newIndex = index * 2 + 1

            else:
                newIndex = index * 2 + 2

            if self.__heap[newIndex] > self.__heap[index]:
                self.__heap[newIndex], self.__heap[index] = self.__heap[index], self.__heap[newIndex]
                index = newIndex
                continue

            break
        

    def __checkPriorityParents(self, index):
        while index != 0:
            if self.__heap[index] > self.__heap[math.ceil(index / 2 - 1)]:
                newIndex = math.ceil(index / 2 - 1)
                self.__heap[index], self.__heap[newIndex] = self.__heap[newIndex], self.__heap[index]
                index = newIndex
                continue

            break


def testAdd():
    heap = Heap(100)
    
    heap.add(68)
    assert heap.index(1) == 68, f"heap.index(1) should be equal 68, but equal {heap.index(1)}"
    assert heap.count == 2, f"heap.count should be equal 2, but equal {heap.count}"
    
    heap.add(93)
    assert heap.index(2) == 93, f"heap.index(2) should be equal 93, but equal {heap.index(2)}"
    assert heap.count == 3, f"heap.count should be equal 3, but equal {heap.count}"

    heap.add(38)
    assert heap.index(3) == 38, f"heap.index(3) should be equal 38, but equal {heap.index(3)}"
    assert heap.count == 4, f"heap.count should be equal 4, but equal {heap.count}"

    heap.add(123)
    assert heap.index(0) == 123, f"heap.index(0) should be equal 123, but equal {heap.index(0)}"
    assert heap.count == 5, f"heap.count should be equal 5, but equal {heap.count}"

    heap.add(100)
    assert heap.index(2) == 100, f"heap.index(2) should be equal 100, but equal {heap.index(2)}"
    assert heap.count == 6, f"heap.count should be equal 6, but equal {heap.count}"

    heap.add(82)
    assert heap.index(6) == 82, f"heap.index(6) should be equal 82, but equal {heap.index(6)}"
    assert heap.count == 7, f"heap.count should be equal 7, but equal {heap.count}"

    heap.add(108)
    assert heap.index(1) == 108, f"heap.index(1) should be equal 108, but equal {heap.index(1)}"
    assert heap.count == 8, f"heap.count should be equal 8, but equal {heap.count}"

    #print(heap.heap())
    print("Test (add) completed", heap.heap())


def testSearch():
    heap = Heap(100)

    heap.add(99)
    heap.add(78)
    heap.add(35)
    heap.add(14)
    heap.add(56)

    result = heap.search(78)
    assert result == 2, f"result should be equal 1, but equal {result}"

    result = heap.search(14)
    assert result == 4, f" result should be equal 3, but equal {result}"

    result = heap.search(100)
    assert result == 0, f"result should be equal 0, but equal {result}"

    result = heap.search(105)
    assert result == None, f"result should be equal None, but equal {result}"

    print("Test (search) completed", heap.heap())


def testPop():
    heap = Heap(100)

    heap.add(99)
    heap.add(78)
    heap.add(35)
    heap.add(14)
    heap.add(56)

    heap.pop()
    assert heap.index(0) == 99, f"heap.index(0) should be equal 99, but equal {heap.index(0)}"
    assert heap.count == 5, f"heap.count should be equal 5, but equal {heap.count}"

    heap.pop()
    assert heap.index(0) == 78, f"heap.index(0) should be equal 78, but equal {heap.index(0)}"
    assert heap.count == 4, f"heap.count should be equal 4, but equal {heap.count}"

    heap.pop()
    assert heap.index(0) == 56, f"heap.index(0) should be equal 56, but equal {heap.index(0)}"
    assert heap.count == 3, f"heap.count should be equal 3, but equal {heap.count}"

    heap.pop()
    assert heap.index(0) == 35, f"heap.index(0) should be equal 35, but equal {heap.index(0)}"
    assert heap.count == 2, f"heap.count should be equal 2, but equal {heap.count}"

    heap.pop()
    assert heap.index(0) == 14, f"heap.index(0) should be equal 14, but equal {heap.index(0)}"
    assert heap.count == 1, f"heap.count should be equal 1, but equal {heap.count}"

    print("Test (pop) completed", heap.heap())


#testAdd()
#testSearch()
#testPop()