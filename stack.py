
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(value, "pushed into stack")

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
        else:
            print("Popped element:", self.stack.pop())

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])

    def reverse_string(self, string):
        s = []
        for ch in string:
            s.append(ch)

        result = ""
        while s:
            result += s.pop()

        print("Reversed string:", result)

    def reverse_stack(self):
        temp = []

        while self.stack:
            temp.append(self.stack.pop())

        self.stack = temp
        print("Stack reversed successfully")


s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String")
    print("5. Reverse Stack")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        string = input("Enter string: ")
        s.reverse_string(string)

    elif choice == 5:
        s.reverse_stack()

    elif choice == 6:
        break

    else:
        print("Invalid choice")
