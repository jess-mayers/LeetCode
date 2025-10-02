class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: TreeNode = None):
        self.root = root

    #############
    # Traversals
    #############
    @staticmethod
    def __inorder(node: TreeNode) -> list:
        if node is None:
            return []
        # recurse left
        # root
        # recurse right
        return Tree.__inorder(node.left) + [node.val] + Tree.__inorder(node.right)

    def inorder(self) -> list:
        return self.__inorder(self.root)

    @staticmethod
    def __preorder(node: TreeNode) -> list:
        if node is None:
            return []
        # root
        # recurse left
        # recurse right
        return [node.val] + Tree.__inorder(node.left) + Tree.__inorder(node.right)

    def preorder(self) -> list:
        return self.__preorder(self.root)

    @staticmethod
    def __postorder(node: TreeNode) -> list:
        if node is None:
            return []
        # recurse left
        # recurse right
        # root
        return Tree.__inorder(node.left) + Tree.__inorder(node.right) + [node.val]

    def postorder(self) -> list:
        return self.__postorder(self.root)

    @staticmethod
    def __level_order(node: TreeNode) -> list:
        pass # TODO

    def level_order(self):
        return self.__level_order(self.root)


class BinarySearchTree(Tree):
    def __init__(self, root: TreeNode = None):
        super().__init__(root)
