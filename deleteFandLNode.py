
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def print_list(self, node):
        if node is None:
            return

        self.print_list(node.next)
        print(node.data, end=" ")

    def print_first_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        first = self.head.data
        current = self.head

        while current.next is not None:
            current = current.next

        last = current.data

        print("First node :", first)
        print("Last node :", last)


# Create the linked list
sll = SinglyLinkedList()

sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(40)
sll.insert(50)

# Print the original linked list
print("Original linked list:")
current = sll.head

while current is not None:
    print(current.data, end=" ")
    current = current.next

print("\n")

# Print first and last nodes
sll.print_first_last()

# Print in reverse order
print("\nReverse order:")
sll.print_list(sll.head)
print()
