
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList: 
    def __init__(self):
        self.head = None
     # Insert at the end of the circular linked list
    def insert(self, data): 
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")

    # Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node 

    # Delete a node by value
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        while True:
            if current.data == value:
                # Only one node
                if current.next == self.head:
                    self.head = None

                # Delete the head node
                elif current == self.head:
                    last = self.head

                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head

                # Delete any other node
                else:
                    previous.next = current.next

                print(value, "deleted")
                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print(value, "not found")

    # Search for a value
    def search(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        position = 1

        while True:
            if current.data == value:
                print(value, "found at position", position)
                return

            current = current.next
            position += 1

            if current == self.head:
                break

        print(value, "not found")

    # Reverse the circular linked list
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        previous = None
        current = self.head
        old_head = self.head

        while True:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

            if current == old_head:
                break

        old_head.next = previous
        self.head = previous


# Main program
cll = SinglyCircularLinkedList()

cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

print("Original Circular Linked List:")
cll.display()

print("\nAfter inserting 5 at the beginning:")
cll.insert_beginning(5)
cll.display()

print("\nSearching for 30:")
cll.search(30)

print("\nDeleting 20:")
cll.delete(20)
cll.display()

print("\nReversed Circular Linked List:")
cll.reverse()
cll.display()
