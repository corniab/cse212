class BST:
    def __init__(self) -> None:
        """Initializes a new Binary Search Tree."""
        self._size = 0
        self.root = None
    
    @property
    def size(self):
        """A getter to return the size of the BST."""
        return self._size

    @property
    def empty(self):
        """A getter to check if the BST is empty."""
        return self._size == 0

    class Node:
        def __init__(self, data) -> None:
            """Initializes a new Node."""
            self.data = data
            self.left = None
            self.right = None

        def __str__(self) -> str:
            return self.data

    def insert(self, data):
        """Inserts data into the BST."""
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        """Look for location to insert data."""
        if data < node.data:
            if node.left is None:
                self._size += 1
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                self.size += 1
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
        else:
            return

    def __contains__(self, data):
        """Checks if BST contains data."""
        return self._contains(data, self.root)


    def _contains(self, data, node):
        """Searches BST for data."""        
        if data < node.data:
            if node.left == None:
                return False
            else:
                return self._contains(data, node.left)
        elif data > node.data:
            if node.right == None:
                return False
            else:
                return self._contains(data, node.right)
        else:
            return True

    def __iter__(self):
        """Iterate through linked list."""
        yield from self._traverse_forward(self.root)

    def __reversed__(self):
        """Iterates backwards through linked list."""
        yield from self._traverse_backward(self.root)

    def _traverse_forward(self, node):
        """Steps left to right through the BST."""
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def _traverse_backward(self, node):
        """Steps right to left throught the BST."""
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
