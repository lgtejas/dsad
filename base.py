# Tree Node Data structure
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Node(TreeNode):

    def __init__(self, data):
        super().__init__(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res
