class LinkedList:
    def __init__(self) -> None:
        """Initializes a new linked list."""
        self.head = None
        self.tail = None
        self.__size = 0

    @property
    def size(self):
        """A getter for returning the size of the linked list."""
        return self.__size

    @property
    def empty(self):
        """A property that checks if the linked list is empty."""
        if self.__size > 0:
            return False
        return True
    
    class Node:
        def __init__(self, data) -> None:
            """Initializes a new node."""
            self.data = data
            self.next = None
            self.prev = None
    
    def insert_head(self, value):
        """Inserts a node before the head."""
        # Create a new node
        node = LinkedList.Node(value)

        # If list is empty then assign head and tail to node.
        if self.head is None:
            self.head = node
            self.tail = node        
        else:
            # Update the pointers.
            node.next = self.head
            self.head.prev = node
            self.head = node

        # Increment the size.
        self.__size += 1

    def insert_tail(self, value):
        """Insert a value after the tail."""
        # Create a new node.
        node = LinkedList.Node(value)

        # If the list is empty 
        # then assign head and tail to node.
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            # Update the pointers.
            node.prev = self.tail
            self.tail.next = node
            self.tail = node          

        # Increment the size.
        self.__size += 1

    def remove_head(self):
        """Deletes the first node."""
        # If the list is empty or has 1 item
        # then set the head and tail to None. 
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Update the pointers.
            self.head = self.head.next 
            self.head.prev = None

        # Decrement the size.
        if self.__size > 0:
            self.__size -= 1

    def remove_tail(self):
        """Removes the last node."""
        # If the list is empty or has 1 item
        # then set the head and tail to None.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Update the pointers.
            self.tail = self.tail.prev
            self.tail.next = None

        # Decrement the size.
        if self.__size > 0:
            self.__size -= 1

    def insert(self, value, index):
        """
        Inserts node at specified index.
        Index is 0 based.
        """

        # Raise exception if index out of range.
        if index < 0 or index > self.__size-1:            
            raise IndexError(f"{index} is out of range.")

        # If index is 0 then insert at head
        if index == 0:
            self.insert_head(value)
            return
        
        # Create a new node
        node = LinkedList.Node(value)

        # Traverse to node before index.
        curr = self.head
        while index > 1:
            curr = curr.next
            index -= 1

        # Update the pointers.
        node.prev = curr
        node.next = curr.next
        curr.next = node
        curr.next.prev = node

        # Increment the size.
        self.__size += 1

    def delete(self, index):
        """
        Deletes node at specified index.
        Index is 0 based.
        """
        # Raise exception if index out of range.
        if index < 0 or index > self.__size:            
            raise IndexError(f"{index} is out of range.")

        # If index is 0 then delete head.
        if index == 0:
            self.remove_head()
            return
        # If index is equal to size then delete tail.
        elif index == self.__size-1:
            self.remove_tail()
            return

        # Traverse to node to be deleted.
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1

        # Update the pointers.
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        # Decrement the size.
        if self.__size > 0:
            self.__size -= 1

    def __iter__(self):
        """Iterate foward through the Linked List."""
        curr = self.head 
        while curr is not None:
            yield curr.data  
            curr = curr.next 

    def __str__(self):
        """Return a string representation of the linked list."""
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


linkedList = LinkedList()

