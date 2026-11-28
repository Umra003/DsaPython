
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
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
        print("Node inserted at end")


    # 3. Insert at a given position
    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted at position", pos)


    # 4. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        self.head = self.head.next

        print("Deleted node:", temp.data)


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

        while temp.next.next is not None:
            temp = temp.next

        print("Deleted node:", temp.next.data)
        temp.next = None


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

        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        deleted = temp.next
        temp.next = deleted.next

        print("Deleted node:", deleted.data)


    # 7. Display / Traversal
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        print("Linked List:")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


    # 8. Count nodes
    def count(self):
        temp = self.head
        total = 0

        while temp is not None:
            total += 1
            temp = temp.next

        print("Total nodes:", total)


# Main program
sll = SinglyLinkedList()

while True:
    print("\n----- SINGLY LINKED LIST -----")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Display / Traversal")
    print("8. Count Nodes")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            sll.insert_beginning(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            sll.insert_end(data)

        elif choice == 3:
            data = int(input("Enter data: "))
            pos = int(input("Enter position: "))
            sll.insert_position(data, pos)

        elif choice == 4:
            sll.delete_beginning()

        elif choice == 5:
            sll.delete_end()

        elif choice == 6:
            pos = int(input("Enter position: "))
            sll.delete_position(pos)

        elif choice == 7:
            sll.display()

        elif choice == 8:
            sll.count()

        elif choice == 9:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")
