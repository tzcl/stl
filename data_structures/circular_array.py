"""
CircularArray implements a circular array in Python.

This enables O(1) insertion and deletion at either the head or the tail of the
array.

This was tested with https://leetcode.com/problems/design-linked-list/
"""


class CircularArray:
    def __init__(self, size=1):
        self.size = size

        self.data = [0] * self.size
        self.start = 0
        self.end = 0
        self.count = 0

    def __repr__(self) -> str:
        return f"CircularArray({self.data[self.start : self.end]})"

    def __getitem__(self, index: int) -> int:
        if index < 0:
            index += self.count
        if index < 0 or index >= self.count:
            raise IndexError("list index out of range")

        return self.data[(self.start + index) % self.size]

    def _resize(self, size) -> None:
        data = [0] * size

        for i in range(self.count):
            data[i] = self.data[(self.start + i) % self.size]

        self.size = size

        # Reset pointers
        self.start = 0
        self.end = self.count
        self.data = data

    def appendleft(self, val: int) -> None:
        if self.count == self.size:
            self._resize(self.size * 2)

        # start is inclusive so we need to decrement then insert
        self.start = (self.start - 1 + self.size) % self.size
        self.data[self.start % self.size] = val
        self.count += 1

    def popleft(self) -> int:
        if self.count == 0:
            raise IndexError("pop from empty list")

        # start is inclusive so we need to read then increment
        elem = self.data[self.start]
        self.start = (self.start + 1) % self.size
        self.count -= 1

        return elem

    def append(self, val: int) -> None:
        if self.count == self.size:
            self._resize(self.size * 2)

        # end is exclusive so we need to insert then increment
        self.data[self.end % self.size] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    def pop(self) -> int:
        if self.count == 0:
            raise IndexError("pop from empty list")

        # end is exclusive so we need to decrement then read
        self.end = (self.end - 1 + self.size) % self.size
        self.count -= 1

        return self.data[self.end]

    def insert(self, index: int, val: int) -> None:
        # This is necessarily O(n) because we need to make room for the new element
        if index < 0 or index >= self.count:
            raise IndexError("list index out of range")

        if self.count == self.size:
            self._resize(self.size * 2)

        # Shift elements to the right
        for i in range(self.count, index, -1):
            curr = (self.start + i) % self.size
            prev = (self.start + i - 1) % self.size
            self.data[curr] = self.data[prev]

        # Insert element
        self.data[(self.start + index) % self.size] = val

        self.end = (self.end + 1) % self.size
        self.count += 1

    def remove(self, index: int) -> None:
        # This is necessarily O(n) because we need to fill in the gap
        if index < 0 or index >= self.count:
            raise IndexError("list index out of range")

        # Shift elements to the left
        for i in range(index, self.count - 1):
            curr = (self.start + i) % self.size
            nxt = (self.start + i + 1) % self.size
            self.data[curr] = self.data[nxt]

        self.end = (self.end - 1 + self.size) % self.size
        self.count -= 1
