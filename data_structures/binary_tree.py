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
    def level_order_traversal(node: Node, level: int, level_to_vals: dict):
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
        new_node = Node(val=val)
        if self.root is None:
            self.root = new_node
            return
        prev = None
        curr = self.root
        while curr is not None:
            prev = curr
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                # no duplicate values allowed
                raise ValueError('Duplicate value detecting in BST')

        if val < prev.val:
            # add to left
            prev.left = new_node
        elif val > prev.val:
            # add to right
            prev.right = new_node

class BinarySearchTreeFactory:
    #############
    # InOrder
    #############
    @staticmethod
    def build_from_inorder(inorder: list) -> Node:
        if len(inorder) == 0:
            return None
        i = inorder.index(max(inorder))
        root = Node(val=inorder[i])
        if len(inorder) == 1:
            return root
        # recurse
        root.left = BinarySearchTreeFactory.build_from_inorder(inorder[:i])
        root.right = BinarySearchTreeFactory.build_from_inorder(inorder[i+1:])
        return root

    #############
    # PreOrder
    #############
    @staticmethod
    def build_from_preorder(preorder: list) -> Node:
        if len(preorder) == 0:
            return None
        root = Node(val=preorder[0])
        if len(preorder) == 1:
            return root
        # find split point
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        # recurse
        root.left = BinarySearchTreeFactory.build_from_preorder(preorder[1:i])
        root.right = BinarySearchTreeFactory.build_from_preorder(preorder[i:])
        return root



    #############
    # PostOrder
    #############
    @staticmethod
    def build_from_postorder(postorder: list) -> Node:
        if len(postorder) == 0:
            return None
        root = Node(postorder[0])
        if len(postorder) == 1:
            return root