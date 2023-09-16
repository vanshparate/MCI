class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.prev = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # Head will point to new node
            self.tail = self.head  # Tail will point to head of new node
            self.length = 1
            return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.next = self.head  # We make the next of the new node point to the present head
            self.head.prev = new_node  # We establish a two-way link by making the previous of the present head point to the new node
            self.head = new_node  # Finally we update the head
            self.length += 1
            return

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
        if position == 0:
            self.prepend(data)  # Inserting at position 0 is equivalent to prepending. So instead of repeating code, we simply call the prepend method
            return
        if position >= self.length:
            if position > self.length:
                print('This position is not available. Inserting at the end of the list')
            self.append(data)  # Similarly, inserting at a position >= the length of the list is equivalent to appending, so we call the append method
            return
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1):  # We traverse upto one position before the position where we want to insert the new node
                current_node = current_node.next
            new_node.prev = current_node  # We make the previous of the new node point to the current node
            new_node.next = current_node.next  # And the next point to the next of the current node.
            current_node.next = new_node  # Then we break the link between the current node and the next node and make the next of the current node point to the new node
            new_node.next.prev = new_node  # And finally we update the previous of the next node to point to the new node instead of the current node. This way, the new node gets inserted in betwwen the current and the next nodes.
            self.length += 1
            return

    def delete_by_value(self, data):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head is None or self.head.next is None:  # If after deleting the first node the list becomes empty or there remains only one node, we set the tail equal to the head
                self.tail = self.head
            if self.head is not None:
                self.head.previous = None  # We set the previous pointer of the new head to be None
            self.length -= 1
            return
        try:  # Try block required as if the value is not found then current_node.next will be None and there is no data parameter to compare.
            while current_node is not None and current_node.next.data != data:
                current_node = current_node.next
            if current_node is not None:
                current_node.next = current_node.next.next
                if current_node.next is not None:  # If the node deleted is not the last node(i.e., the node next to the next to the current node is !- None),
                    current_node.next.previous = current_node  # Then we set the previous of the node next to the deleted node equal to the current node, so a two-way link is established
                else:
                    self.tail = current_node  # If the deleted node is the last node then we update the tail to be the current node
                self.length -= 1
                return
        except AttributeError:
            print("Given value not found.")
            return

    def delete_by_position(self, position):
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        if position == 0:
            self.head = self.head.next
            # print(self.head)
            if self.head is None or self.head.next is None:
                self.tail = self.head
            if self.head is not None:
                self.head.previous = None  # We update the previous of the new head to be equal to None
            self.length -= 1
            return

        if position >= self.length:
            position = self.length - 1

        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next is not None:  # Similar logic to the delete_by_value method
            current_node.next.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return


# I'll create a Doubly linked list and call all its methods in the same sequence as I did in the Singly Linked List implementation
# The answers should come out to be the same
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
# This position is not available. Inserting at the end of the list
# 0 4 5 7 2 9 0 3

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

my_linked_list.delete_by_value(3)
my_linked_list.print_list()
# Given value not found.

print(my_linked_list.length)
# 3
