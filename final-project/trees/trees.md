# Tree

> “Computers are good at following instructions, but not at reading your mind.”
> ― Donald Knuth[^1]

## Usage

Lets take a moment imagine a family tree. At the top of our tree are the primary ancestor. All the generations below them are their descendants. Directly below them are their children. The children are siblings, meaning that they share the same parents. This pattern can continue indefinitely.

![family tree](../resources/family-tree.jpg)

Trees, in computer science, are a data structure made up of nodes connected in a hierarchical tree like fashion.[^2] There is a single "root" node. Each node may have 0 or more "child" nodes. Binary Search Trees are a specialized type of tree that allows each node to have 0 to two "child" nodes.
![tree data structure](../resources/tree.jpg)

Trees are commonly used data structures for when we have hierarchical data. They are also good at insertion and searching for data.[^3] As you can imagine this can be useful several types of application.

- File Systems
- Document Object Model in Web Browsers
- Hierarchy of classes in Object Oriented Programming.

## Time Complexity of Binary Search Tree[^4]

|     Operation      | Description                                | Time Complexity |
| :----------------: | :----------------------------------------- | :-------------: |
|   insert(value)    | Insert a value into a tree                 |    O(log n)     |
|   remove(value)    | Remove a value from the tree               |    O(log n)     |
|  contains(value)   | Determine if a value is in the tree        |    O(log n)     |
| traverse_forward() | Visit all objects from smallest to largest |      O(n)       |
| traverse_reverse() | Visit all objects from largest to smallest |      O(n)       |
|    height(node)    | Determine if the height of a node          |      O(n)       |
|       size()       | Return the size of the BST                 |      O(1)       |
|      empty()       | Returns true if the root node is empty     |      O(1)       |

## Example

```python
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
```

## Practice Problem

For our practice problem, we will use a generic tree that uses arrays to store its child nodes.
This will increase the time complexity of insertion and removal to O(n).

```python

```

You can find the solution [here](solution.py).

### Footnotes

[^1]: Quote by Donald Knuth, [AZ Quotes](https://www.azquotes.com/quote/562000)
[^2]: Tree Data Structure, [Wikipedia](<https://en.wikipedia.org/wiki/Tree_(data_structure)>)
[^3]: Introduction To Binary Trees, [Study Tonight](https://www.studytonight.com/data-structures/introduction-to-binary-trees)
[^4]: Trees, [BYU-I CSE 212 Course Notes](https://byui-cse.github.io/cse212-course/lesson09/09-prepare.html)
[^5]: []()
