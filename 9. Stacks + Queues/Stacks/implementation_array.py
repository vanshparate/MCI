class Node():
    def __init__(self, data):
        self.length = 0
        self.data = {}


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            print("Stack empty")
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None

    def print_stack(self):
        if self.top is None:
            return "Stack is Empty"
        else:
            current_pointer = self.top
            while current_pointer is not None:
                print(current_pointer.data)
                current_pointer = current_pointer.next


my_stack = Stack()

print(my_stack.peek())
# None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()

print(my_stack.top.data)
print(my_stack.bottom.data)

my_stack.pop()
my_stack.print_stack()
# udemy
# google

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
