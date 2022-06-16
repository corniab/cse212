# Week 9 Notes - Trees4

Trees are similar to linked lists in that they contain nodes that point to each other.
Data is stored in a hierarchical structure (tree-like) vs a linear structure (list-like).
Structured by level 0..n

## Advantages

Binary Search Trees have faster lookups than arrays or linked lists. They are great for storing sorted data.

## Scenarios for deletion

1. Delete node with no child
2. Delete node with one child
3. Delete node with two children
   - requires you to rebalance tree.
   - find minimum node in left subtree and copy it and remove duplicates
   - or find maximum value in right subtree and copy and remove duplicates

## Resources

- [Binary Tree Part 1](https://youtu.be/lFq5mYUWEBk)
- [Binary Tree Part 2](https://youtu.be/JnrbMQyGLiU)

## Common Operations

| Operation        | Description                                                                                      | Performance |
| :--------------- | :----------------------------------------------------------------------------------------------- | :---------: |
| insert(value)    | Insert a value into the tree.                                                                    |  O(log n)   |
| remove(value)    | Remove a value from the tree.                                                                    |  O(log n)   |
| contains(value)  | Determine if a value is in the tree                                                              |  O(log n)   |
| traverse_forward | Visit all objects from smallest to largest.                                                      |    O(n)     |
| traverse_reverse | Visit all objects from largest to smallest.                                                      |    O(n)     |
| height(node)     | Determine the height of the node. If the height of the tree is needed, the root node is provided |    O(n)     |
| size()           | Return the size of the BST.                                                                      |    O(1)     |
| empty()          | Returns true if the root node is empty. This can also be done by checking the size for 0         |    O(n)     |

## Definitions

- AVL Tree: Adelson-Velskii and Landis Tree. A balanced binary search tree that is checked unbalanced height after every modification to the tree. If the tree is unbalanced, then pre-determined algorithms are used to balance the tree.
- balanced: A tree is balanced if the height of the tree from the root to each leaf is consistent for all subtrees. The measure of consistency will vary between algorithms but usually does not exceed a height difference of 1.
- balanced binary search tree: A binary search tree which is balanced or restructured to be balanced. A balanced binary search tree has O(log n) performance when searching
- binary search tree: A binary tree that puts data less than the root to the left and greater than the root to the right. This type of a tree enables searching algorithms to be efficient.
- binary tree: A tree that has up to two children for each node.
- child: a child is a node connected from a parent node.
- leaf: a leaf is a node that has no children.
- node: an entry in a tree that contains bothe value and pointers to any children nodes.
- parent: a parent is a node that connects to children nodes
- root: the first parent in a tree.
- subtree: Subset of a tree made by selecting a node to be the root and including all the children from that node.
- traverse: the process of visiting all nodes (and subsequently their values) in a tree. Used frequently with a binary search tree using recursion to start at the leaf node that containse the smallest value and going to the leaf node that contains the largest value.
- trees: a data structure that starts with a root node and is subsequently connected to multiple nodes according to a relationship between the nodes. The tree does not have any circular loops or unconnected nodes.
