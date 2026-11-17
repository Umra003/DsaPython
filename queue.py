class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted into queue")

    def dequeue(self):
        if not self.queue:
            print("Queue Underflow")
        else:
            print("Deleted element:", self.queue.pop(0))

    def display(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

    def reverse_queue(self):
        stack = []

        while self.queue:
            stack.append(self.queue.pop(0))

        while stack:
            self.queue.append(stack.pop())

        print("Queue reversed:", self.queue)

    def merge_queues(self, q2):
        merged = self.queue + q2.queue
        print("Merged Queue:", merged)

    def identical(self, q2):
        if self.queue == q2.queue:
            print("Queues are identical")
        else:
            print("Queues are not identical")


q1 = Queue()
q2 = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue")
    print("5. Merge Two Queues")
    print("6. Check Identical")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        q1.enqueue(value)

    elif choice == 2:
        q1.dequeue()

    elif choice == 3:
        q1.display()

    elif choice == 4:
        q1.reverse_queue()

    elif choice == 5:
        n = int(input("Enter number of elements in second queue: "))

        for i in range(n):
            value = int(input("Enter element: "))
            q2.enqueue(value)

        q1.merge_queues(q2)

    elif choice == 6:
        q1.identical(q2)

    elif choice == 7:
        break

    else:
        print("Invalid choice")	 
