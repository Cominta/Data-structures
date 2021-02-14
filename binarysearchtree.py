class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree():
    def __init__(self, rootValue):
        self.root = Node(rootValue)
        self.count = 1 # Количество элементов
        self.height = 0  # Высота дерева (если посмотреть на визуализацию)

    
    def add(self, value):
        if self.root.right == None and self.root.left == None:
            if value >= root:
                self.root.right = Node(value)
            
            else:
                self.root.left = Node(value)

        node = self.root
        for i in range(self.height):
            if value > node.right:
                node = node.right
            
            else:
                node = node.left
        
        print(node.value)


def testAdd():
    tree = BinarySearchTree(10)

    tree.add(5)
    assert tree.root.left == 5, "tree.root.left should be equal 5, add"

    tree.add(14)
    assert tree.root.right == 14, "tree.root.right should be equal 14, add"

    tree.add(16)
    assert tree.root.right.right == 16, "tree.root.right.right should be equal 16, add"

    print("Test (add) completed")


testAdd()