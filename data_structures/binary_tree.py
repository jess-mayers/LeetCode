class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    #############
    # Traversals
    #############
    @staticmethod
    def __inorder(node: Node) -> list:
        if node is None:
            return []
        # recurse left
        # root
        # recurse right
        return BinaryTree.__inorder(node.left) + [node.val] + BinaryTree.__inorder(node.right)

    def inorder(self) -> list:
        return self.__inorder(self.root)

    @staticmethod
    def __preorder(node: Node) -> list:
        if node is None:
            return []
        # root
        # recurse left
        # recurse right
        return [node.val] + BinaryTree.__inorder(node.left) + BinaryTree.__inorder(node.right)

    def preorder(self) -> list:
        return self.__preorder(self.root)

    @staticmethod
    def __postorder(node: Node) -> list:
        if node is None:
            return []
        # recurse left
        # recurse right
        # root
        return BinaryTree.__inorder(node.left) + BinaryTree.__inorder(node.right) + [node.val]

    def postorder(self) -> list:
        return self.__postorder(self.root)

    @staticmethod
    def __level_order(node: Node) -> list:
        pass # TODO

    def level_order(self):
        return self.__level_order(self.root)


class BinarySearchTree(BinaryTree):
    def __init__(self, root: Node = None):
        super().__init__(root)

    def insert(self, val: int):
        # TODO
        pass