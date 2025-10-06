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
    def inorder_traversal(node: Node) -> list:
        if node is None:
            return []
        # recurse left
        # root
        # recurse right
        return BinaryTree.inorder_traversal(node.left) + [node.val] + BinaryTree.inorder_traversal(node.right)

    def inorder(self) -> list:
        return self.inorder_traversal(self.root)

    @staticmethod
    def preorder_traversal(node: Node) -> list:
        if node is None:
            return []
        # root
        # recurse left
        # recurse right
        return [node.val] + BinaryTree.inorder_traversal(node.left) + BinaryTree.inorder_traversal(node.right)

    def preorder(self) -> list:
        return self.preorder_traversal(self.root)

    @staticmethod
    def postorder_traversal(node: Node) -> list:
        if node is None:
            return []
        # recurse left
        # recurse right
        # root
        return BinaryTree.inorder_traversal(node.left) + BinaryTree.inorder_traversal(node.right) + [node.val]

    def postorder(self) -> list:
        return self.postorder_traversal(self.root)

    @staticmethod
    def level_order_traversal(node: Node, level: int, level_to_vals: dict) -> list:
        if node is None:
            return
        # add list if index does not exist
        if not level_to_vals.get(level):
            level_to_vals[level] = []

        level_to_vals[level].append(node.val)
        BinaryTree.level_order_traversal(node.left, level + 1, level_to_vals)
        BinaryTree.level_order_traversal(node.right, level + 1, level_to_vals)

    def level_order(self) -> list:
        level_to_vals = {}
        self.level_order_traversal(self.root, 0, level_to_vals)
        level_order = []
        for level in sorted(level_to_vals):
            level_order.extend(level_to_vals[level])
        return level_order


class BinarySearchTree(BinaryTree):
    def __init__(self, root: Node = None):
        super().__init__(root)

    def insert(self, val: int):
        # TODO
        pass

class BinarySearchTreeFactory:
    @staticmethod
    def build_from_inorder(l: list) -> BinarySearchTree:
        pass # TODO

    @staticmethod
    def build_from_preorder(l: list) -> BinarySearchTree:
        pass # TODO

    @staticmethod
    def build_from_postorder(l: list) -> BinarySearchTree:
        pass # TODO