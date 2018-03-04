""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    if root.data == None:
        return True
    else:
        return BST(root, float('-inf'), float('inf'))


def BST(node, min_key, max_key):
    if node.data <= min_key:
        return False
    if node.data >= max_key:
        return False
    left_ok = True
    right_ok = True

    if node.left is not None:
        left_ok = BST(node.left, min_key, node.data)
    if node.right is not None:
        right_ok = BST(node.right, node.data, max_key)
    return left_ok and right_ok