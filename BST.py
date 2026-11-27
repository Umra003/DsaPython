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

# LEVEL-WISE COUNTING
    def count_level_wise(self, root):
        if root is None:
            print("Tree is empty")
            return

        queue = [root]
        level = 0

        while queue:
            level_count = len(queue)

            print("Level", level, ":", level_count, "nodes")

            for i in range(level_count):
                node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            level += 1

# MAIN PROGRAM

tree = BST()

n = int(input("How many nodes do you want to insert? "))

for i in range(n):
    value = int(input("Enter node value: "))
    tree.root = tree.insert(tree.root, value)


while True:

    print("\n----- BST OPERATIONS -----")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Delete")
    print("7. Count Total Nodes")
    print("8. Count Left Subtree Nodes")
    print("9. Count Right Subtree Nodes")
    print("10. Count Nodes Level-wise")
    print("11. Find Minimum")
    print("12. Find Maximum")
    print("13. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        tree.root = tree.insert(tree.root, value)
        print("Node inserted successfully")

    elif choice == 2:
        key = int(input("Enter value to search: "))

        if tree.search(tree.root, key):
            print("Value found")
        else:
            print("Value not found")

    elif choice == 3:
        print("Inorder:")
        tree.inorder(tree.root)
        print()

    elif choice == 4:
        print("Preorder:")
        tree.preorder(tree.root)
        print()

    elif choice == 5:
        print("Postorder:")
        tree.postorder(tree.root)
        print()

    elif choice == 6:
        value = int(input("Enter value to delete: "))
        tree.root = tree.delete(tree.root, value)
        print("Deletion operation completed")

    elif choice == 7:
        print("Total nodes:", tree.count_nodes(tree.root))

    elif choice == 8:
        print("Left subtree nodes:",
              tree.count_left_subtree(tree.root))

    elif choice == 9:
        print("Right subtree nodes:",
              tree.count_right_subtree(tree.root))

    elif choice == 10:
        tree.count_level_wise(tree.root)

    elif choice == 11:
        result = tree.find_min(tree.root)

        if result is None:
            print("Tree is empty")
        else:
            print("Minimum value:", result.data)

    elif choice == 12:
        result = tree.find_max(tree.root)

        if result is None:
            print("Tree is empty")
        else:
            print("Maximum value:", result.data)

    elif choice == 13:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

