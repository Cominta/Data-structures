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