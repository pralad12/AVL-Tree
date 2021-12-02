class Node():
    def __init__(self, key, value):
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1
        self.key = key
        self.value = value


# Problem 0 - implement an AVL tree
# Problem 0 - implement an AVL tree
class AVLTree():
    def __init__(self):
        self.size = 0
        self.root = None
        self.recInsCount = 0

    def getSize(self):
        return self.size

    def searchKey(self, node, key):
        if key == node.key:
            return True
        elif key < node.key:
            if node.left is None:
                return False
            else:
                return self.searchKey(node.left, key)
        else:
            if node.right is None:
                return False
            else:
                return self.searchKey(node.right, key)

    def hasKey(self, key):
        if self.root is None:
            return False
        else:
            return self.searchKey(self.root, key)

    def valFromKey(self, node, key):
        if key == node.key:
            return node.value
        if key < node.key:
            if node.left is None:
                return None
            else:
                return self.valFromKey(node.left, key)
        if key > node.key:
            if node.right is None:
                return None
            else:
                return self.valFromKey(node.right, key)

    def getKey(self, key):
        if self.root is None:
            return None
        else:
            return self.valFromKey(self.root, key)

    def rightRotate(self, node):
        child = node.left
        temp = child.right
        if node.parent is not None:
            node.parent.left = child
            child.parent = node.parent
            node.parent = child

        else:
            self.root = child
            child.parent = None
        child.right = node
        # node.parent = child
        node.left = temp
        if temp is not None:
            temp.parent = node
            temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))

    def leftRotate(self, node):
        child = node.right
        temp = child.left
        if node.parent is not None:
            node.parent.left = child
            child.parent = node.parent
            node.parent = child
        else:
            self.root = child
            child.parent = None
        child.left = node
        # node.parent = child
        node.right = temp
        if temp is not None:
            temp.parent = node
            temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))

    def rightLeft(self, node):
        gChild = node.right.left
        child = node.right
        self.rightRotate(child)
        temp = gChild.left
        if node.parent is not None:
            node.parent.right = gChild
            gChild.parent = node.parent
            node.parent = gChild
        else:
            self.root = gChild
            gChild.parent = None
        gChild.left = node
        # node.parent = child
        node.right = temp
        if temp is not None:
            temp.parent = node
            temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))
        gChild.height = 1 + max(self.getHeight(gChild.left), self.getHeight(gChild.right))

    def leftRight(self, node):
        gChild = node.left.right
        child = node.left
        self.leftRotate(child)
        temp = gChild.right
        if node.parent is not None:
            node.parent.left = gChild
            gChild.parent = node.parent
            node.parent = gChild
        else:
            self.root = gChild
            gChild.parent = None
        gChild.right = node
        node.left = temp
        if temp is not None:
            temp.parent = node
            temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))
        gChild.height = 1 + max(self.getHeight(gChild.left), self.getHeight(gChild.right))

    def insert(self, node, key, value):
        self.recInsCount += 1
        if key == node.key:
            node.value = value
        # if key is less than node.key node go to left side
        if key < node.key:
            # if the node does not have a left child, insert a node with the specified key and value
            if node.left is None:
                node.left = Node(key, value)
                node.left.parent = node
                self.size += 1

            else:
                self.insert(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value)
                node.right.parent = node
                self.size += 1


            else:
                self.insert(node.right, key, value)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        balance = self.getBalance(node)

        # left left
        if balance > 1 and key < node.left.key:
            self.rightRotate(node)


        # right right
        elif balance < -1 and key > node.right.key:
            self.leftRotate(node)


        # left right
        elif balance > 1 and key > node.left.key:
            self.leftRight(node)

        # right left
        elif balance < -1 and key < node.right.key:
            self.rightLeft(node)

    def put(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.root.height = 0
        else:
            self.insert(self.root, key, value)

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)