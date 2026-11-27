
class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # 1. Enqueue
    def enqueue(self, value):

        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")

        else:
            if self.front == -1:
                self.front = 0

            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

            print(value, "inserted into queue")

    # 2. Dequeue
    def dequeue(self):

        if self.front == -1:
            print("Queue Underflow")

        else:
            print("Deleted element:", self.queue[self.front])

            if self.front == self.rear:
                self.front = -1
                self.rear = -1

            else:
                self.front = (self.front + 1) % self.size

    # 3. Display
    def display(self):

        if self.front == -1:
            print("Queue is empty")

        else:
            print("Queue:", end=" ")

            i = self.front

            while True:
                print(self.queue[i], end=" ")

                if i == self.rear:
                    break

                i = (i + 1) % self.size

            print()

    # 4. Peek
    def peek(self):

        if self.front == -1:
            print("Queue is empty")

        else:
            print("Front element:", self.queue[self.front])

    # 5. Reverse Queue
    def reverse_queue(self):

        if self.front == -1:
            print("Queue is empty")

        else:
            temp = []
            i = self.front

            while True:
                temp.append(self.queue[i])

                if i == self.rear:
                    break

                i = (i + 1) % self.size

            temp.reverse()

            self.queue = [None] * self.size

            for i in range(len(temp)):
                self.queue[i] = temp[i]

            self.front = 0
            self.rear = len(temp) - 1

            print("Queue reversed:", temp)

    # 6. Check Empty
    def is_empty(self):

        if self.front == -1:
            print("Queue is empty")

        else:
            print("Queue is not empty")

    # 7. Check Full
    def is_full(self):

        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")

        else:
            print("Queue is not full")


# Creating object
size = int(input("Enter size of queue: "))
q = CircularQueue(size)

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Peek")
    print("5. Reverse Queue")
    print("6. Check Empty")
    print("7. Check Full")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        q.peek()

    elif choice == 5:
        q.reverse_queue()

    elif choice == 6:
        q.is_empty()

    elif choice == 7:
        q.is_full()

    elif choice == 8:
        break

    else:
        print("Invalid choice")
