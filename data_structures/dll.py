class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prv = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.nxt = self.tail
        self.tail.prv = self.head

        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")

        curr = self.head.nxt
        for _ in range(index):
            curr = curr.nxt

        return curr.val

    def appendleft(self, val: int) -> None:
        node = Node(val)

        self.head.nxt.prv = node
        node.nxt = self.head.nxt
        node.prv = self.head
        self.head.nxt = node

        self.size += 1

    def append(self, val: int) -> None:
        node = Node(val)

        self.tail.prv.nxt = node
        node.nxt = self.tail
        node.prv = self.tail.prv
        self.tail.prv = node

        self.size += 1

    def insert(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("list index out of range")

        node = Node(val)

        curr = self.head.nxt
        for _ in range(index):
            curr = curr.nxt

        curr.prv.nxt = node
        node.prv = curr.prv
        node.nxt = curr
        curr.prv = node

        self.size += 1

    def remove(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")

        curr = self.head.nxt
        for _ in range(index):
            curr = curr.nxt

        curr.prv.nxt = curr.nxt
        curr.nxt.prv = curr.prv

        self.size -= 1
