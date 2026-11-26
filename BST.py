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

# POSTORDER
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

# FIND MINIMUM
    def find_min(self, root):
        if root is None:
            return None

        while root.left is not None:
            root = root.left

        return root

# FIND MAXIMUM
    def find_max(self, root):
        if root is None:
            return None

        while root.right is not None:
            root = root.right

        return root

# DELETION
    def delete(self, root, value):
        if root is None:
            return None

        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:
            # Case 1: Leaf node
            if root.left is None and root.right is None:
                return None

            # Case 2: Only right child
            elif root.left is None:
                return root.right

            # Case 2: Only left child
            elif root.right is None:
                return root.left

            # Case 3: Two children
            else:
                successor = self.find_min(root.right)
                root.data = successor.data
                root.right = self.delete(root.right, successor.data)

        return root


    # COUNT TOTAL NODES
    def count_nodes(self, root):
        if root is None:
            return 0

        return (1 + self.count_nodes(root.left)#1 points to the current node.
                  + self.count_nodes(root.right))

    # COUNT LEFT SUBTREE
    def count_left_subtree(self, root):
        if root is None:
            return 0

        return self.count_nodes(root.left)

    # COUNT RIGHT SUBTREE
    def count_right_subtree(self, root):
        if root is None:
            return 0

        return self.count_nodes(root.right)

