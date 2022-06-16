class Doubly_Linked: 
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.size = 0

    def append_left(self, val):
        """Add value before the head."""

    def append(self, val):
        """Add value after the tail."""
        if self.head == None:
            self.head = self.Node(val, self.head, None)
            self.tail = self.head
        else: 
            self.tail +

    def insert(self, index, val):
        """Insert value after index."""

    def pop_left(self):
        """Remove and return the head."""

    def pop(self):
        """Remove and return the tail."""

    def empty(self):
        """Return true if length is zero."""

    def __delitem__(self, index):
        """Remove node at index"""
    
    def __len__(self, obj):
        """Return the size of the linked list."""
        return obj.size

    def __str__(self):
        curr = self.head
        repr = "HEAD"
        for _ in range(self.size):
            repr += " -> " + curr
            curr = curr.next
        return repr + " <- TAIL"

    class Node:
        def __init__(self, data, next, prev) -> None:
            self.data = data
            self.next = next
            self.prev = prev

        def __str__(self) -> str:
            return str(self.data)


    
    
    
    
