# Linked lists are, as the name suggests, a list which is linked.
# It consists of nodes which contain data and a pointer to the next node in the list.
# The list is connected with the help of these pointers.
# These nodes are scattered in memory, quite like the buckets in a hash table.
# The node where the list starts is called the head of theblist and the node where it ends, or last node, is called the tail of the list.
# The average time complexity of some operations invloving linked lists are as follows:
# Look-up : O(n)
# Insert : O(n)
# Delete : O(n)
# Append : O(1)
# Prepend : O(1)
# Python doesn't have a built-in implementation of linked lists, we have to build it on our own

# First we define a class Node which will act as a blueprint for each of our nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # Head will point to new node
            self.tail = self.head  # Tail will point to head of new node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        if self.head is None:
            print("Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print()

    def insert(self, position, data):
        if position >= self.length:
            if position > self.length:
                print("This Position is not available. Inserting at the end of the list.")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def delete_by_value(self, data):
        if self.head is None:
            print("Linked List is empty.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
            return
        while current_node.next is not None and current_node.next.data is not data:
            current_node = current_node.next
        if current_node.next is not None:
            current_node.next = current_node.next.next
            if current_node.next is None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")

    def delete_by_position(self, position):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
            return
        if position >= self.length:
            position = self.length - 1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next is None:
            self.tail = current_node
        return


my_linked_list = LinkedList()
my_linked_list.print_list()
# Empty


my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(9)
my_linked_list.print_list()
# 5 2 9

my_linked_list.prepend(4)
my_linked_list.print_list()
# 4 5 2 9

my_linked_list.insert(2, 7)
my_linked_list.print_list()
# 4 5 7 2 9

my_linked_list.insert(0, 0)
my_linked_list.insert(6, 0)
my_linked_list.insert(9, 3)
my_linked_list.print_list()

my_linked_list.delete_by_value(3)
my_linked_list.print_list()
# 0 4 5 7 2 9 0

my_linked_list.delete_by_value(0)
my_linked_list.print_list()
# 4 5 7 2 9 0

my_linked_list.delete_by_position(3)
my_linked_list.print_list()
# 4 5 7 9 0

my_linked_list.delete_by_position(0)
my_linked_list.print_list()
# 5 7 9 0

my_linked_list.delete_by_position(8)
my_linked_list.print_list()
# 5 7 9
print(my_linked_list.length)
# 3
