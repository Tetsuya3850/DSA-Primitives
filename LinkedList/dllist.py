class DoubleNode:
    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def appendleft(self, new_data):
        new_node = DoubleNode(new_data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, new_data):
        new_node = DoubleNode(new_data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        temp = self.tail
        if not temp:
            return
        data = temp.data
        self.tail = temp.prev
        if not self.tail:
            self.head = None
        else:
            self.tail.next = None
        return data

    def popleft(self):
        temp = self.head
        if not temp:
            return
        data = temp.data
        self.head = temp.next
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def printall(self):
        temp = self.head
        while temp:
            print (temp.data, end=" ")
            temp = temp.next
        print()

dll = DoublyLinkedList()
dll.append(4)
dll.append(3)
dll.appendleft(2)
dll.pop()
dll.pop()
dll.popleft()
dll.appendleft(2)
dll.printall()