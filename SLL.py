
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


# Create the linked list
sll = SinglyLinkedList()

sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(40)
sll.insert(50)

print("Original linked list:")
current = sll.head
while current is not None:
    print(current.data, end=" ")
    current = current.next

print("\nReverse order:")
sll.print_list(sll.head)
