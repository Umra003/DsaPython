class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # INSERTION
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

# SEARCHING
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        elif key < root.data:
            return self.search(root.left, key)

        else:
            return self.search(root.right, key)

# INORDER
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

# PREORDER
    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

# # POSTORDER
#     def postorder(self, root):
#         if root is not None:
#             self.postorder(root.left)
#             self.postorder(root.right)
#             print(root.data, end=" ")

