
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print("Node inserted at beginning")


    # 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Node inserted at end")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        print("Node inserted at end")


    # 3. Insert at a given position
    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_beginning(data)
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print("Node inserted at position", pos)


    # 4. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        print("Deleted node:", temp.data)

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None


    # 5. Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            print("Deleted node:", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        print("Deleted node:", temp.data)

        temp.prev.next = None


    # 6. Delete from a given position
    def delete_position(self, pos):
        if self.head is None:
            print("Linked List is empty")
            return

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.delete_beginning()
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        print("Deleted node:", temp.data)

        temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev


    # 7. Forward traversal
    def display_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        print("Forward Traversal:")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


    # 8. Backward traversal
    def display_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        print("Backward Traversal:")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


    # 9. Count nodes
    def count(self):
        temp = self.head
        total = 0

        while temp is not None:
            total += 1
            temp = temp.next

        print("Total nodes:", total)


# Main program
dll = DoublyLinkedList()

while True:
    print("\n----- DOUBLY LINKED LIST -----")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Forward Traversal")
    print("8. Backward Traversal")
    print("9. Count Nodes")
    print("10. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            dll.insert_beginning(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            dll.insert_end(data)

        elif choice == 3:
            data = int(input("Enter data: "))
            pos = int(input("Enter position: "))
            dll.insert_position(data, pos)

        elif choice == 4:
            dll.delete_beginning()

        elif choice == 5:
            dll.delete_end()

        elif choice == 6:
            pos = int(input("Enter position: "))
            dll.delete_position(pos)

        elif choice == 7:
            dll.display_forward()

        elif choice == 8:
            dll.display_backward()

        elif choice == 9:
            dll.count()

        elif choice == 10:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")
