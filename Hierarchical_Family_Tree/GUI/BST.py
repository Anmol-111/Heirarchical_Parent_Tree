# Implimentation of Binary Search Tree:
class Node:
    def __init__(self, data):
        self.left=None
        self.data = data
        self.right=None

def insert(root, data):
    if root is None:
        return Node(data)
    elif root.data == data:
        return root
    elif root.data < data:
        root.right = insert(root.right, data)
    else:
        root.left = insert(root.left, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end="\n")
        inorder(root.right)

root=Node(50)
root=insert(root, 30)
root=insert(root, 20)
inorder(root)