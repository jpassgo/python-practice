class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:

    def __init__(self, data=None):
        self.head = None
        self.tail = None

    def __str__(self):
        linkedListAsString = ""
        curr = self.head
        while curr is not None:
            linkedListAsString += str(curr.data) + "->"
            curr = curr.next

        if linkedListAsString is not None:
            return "[" + linkedListAsString[:-2] + "]"
        else:
            return "[]"

    def append_val(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.head is None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def add_to_start(self, node):
        temp = self.head
        self.head = node
        node.next = temp

    def search_val(self, x):
        if self.head.data == x:
            return 0

        curr = self.head
        count = 1
        while curr.next is not None:
            if curr.next.data == x:
                return count
            count += 1
            curr = curr.next

    def remove_val_by_index(self, index):
        curr = self.head
        count = 0
        while count <= index and curr.next is not None:
            if count == index:
                temp = curr.next
                curr.next = temp.next
            count += 1
            curr = curr.next

    def length(self):
        curr = self.head
        count = 0
        while curr.next is not None:
            curr = curr.next
            count += 1
        return count

    def reverse_list_recur(self, current, previous):
        pass


node1, node2, node3, node4, node5, = Node(
    1), Node(2), Node(3), Node(4), Node(5)

myList = LinkedList()

myList.append_val(node1)
myList.append_val(node2)
myList.append_val(node3)
myList.append_val(node4)
myList.append_val(5)

print(myList)
print(myList.length())

print(myList.search_val(4))
myList.remove_val_by_index(2)

print(myList)

print(myList.length())

myList.add_to_start(Node(76))
print(myList)
