from Array import Array
from LinkedList import LinkedList

class Graph:
    def __init__(self):
        self.__list = Array(10)


    def addVertex(self, value):
        self.__list.append(LinkedList())
        self.__list.index(self.__list.size - 1).insertToTheEnd(value)
    

    def addEdges(self, mainIndex, *indices):
        for k in range(len(indices)):
            if indices[k] > self.__list.size - 1:
                raise IndexError("Out of range")

            elif indices[k] == mainIndex:
                raise IndexError("It is impossible to connect the vertex to itself")

        if mainIndex > self.__list.size - 1:
            raise IndexError("Out of range")

        for i in range(len(indices)):
            if self.__list.index(mainIndex).search(indices[i]):
                raise IndexError("Vertex already connected")

            self.__list.index(mainIndex).insertToTheEnd(indices[i])
            self.__list.index(indices[i]).insertToTheEnd(mainIndex)