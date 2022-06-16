class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

class Singly_Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append_left(self, val):
        """ Add node to the beginning of the list. """
        self.head = Node(val, self.head)
        self.size += 1

    def append(self, val):
        """ Add node to the end of the list. """
        if self.head == None:
            self.head = Node(val, self.head)
        else:
            curr = self.head
            for _ in range(self.size-1):
                curr = curr.next
            curr.next = Node(val, None)

        self.size += 1

    def pop(self):
        """Remove last node and return it."""
        deleted = None
        if self.size > 1:
            curr = self.head
            for _ in range(self.size-2):
                curr = curr.next
            deleted = curr.next
            curr.next = None
        else:
            deleted = self.head
            self.head = None

        self.size -= 1
        return deleted

    def pop_left(self):
        """Remove first node and return it."""
        deleted = None
        if self.size > 1:
            deleted = self.head
            self.head = self.head.next
            self.size -= 1
        elif self.size == 1:
            deleted = self.head
            self.head = None
            self.size -= 1
        
        
        return deleted
    
    def insert(self, index, val):
        """Insert node"""
        if index == 0 and self.size == 0:
            self.head = Node(val, self.head)
        elif index < 0 or index > self.size-1:
            raise IndexError(f"Index: '{index}' is out of range.")
        if self.size > 0:                 
            curr = self.head
            for _ in range(index):
                curr = curr.next
            next = curr.next
            curr.next = Node(val, next)


        self.size += 1

    def __str__(self) -> str:
        repr_str = "HEAD"
        curr = self.head
        for _ in range(self.size):           
            repr_str += " -> " + str(curr.val)
            curr = curr.next
        return repr_str + " -> NONE"

        

linked_list = Singly_Linked_List()


linked_list.insert(0, "new node")
linked_list.insert(0, "new node after position 0")

print(linked_list)