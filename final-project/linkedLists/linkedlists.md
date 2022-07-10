# Linked List

> "There are no morals about technology at all. Technology expands our ways of thinking about things, expands our ways of doing things. If we're bad people we use technology for bad purposes and if we're good people we use it for good purposes."
> ― Herbert Simon [^1]

Lets take a moment to imagine children lined up outside[^2], waiting to go to class after recess. Their teacher, worried that they will get lost on the way inside, asks each of the children to hold hands with the classmate in front of them and classmate behind them. The child at the front of the line will only hold hands with the child behind them. The child at the back of the line will only hold hands with the child in front of them. It would look something like this.

![Children holding hands in a line.](../resources/children.jpg)

Now, the teacher will only have to keep track of the child at the front and the child at the back, because he knows that the rest are somewhere in the middle. This is similar to how linked lists work.

A linked list is a linear data structure that contains a sequence of nodes[^3]. A node contains data and a reference to the node next to it. Below is an example of a singly linked list (meaning each node only contains one reference).

![Singly Linked List](../resources/singley-linked.jpg)

A doubly linked list contains a reference to the node before and after it. This is what it would look like.

![doubly linked list](../resources/doubly-linked.jpg)

To insert a node into the middle of a linked list we just update the pointers (references) to the appropriate nodes. If we are inserting at the head or tail — then we just update the respective pointer.

![inserting a node into a linked list](../resources/insert-linked.jpg)

Deleting a node from the middle is similar in fashion to inserting. We just update the pointers and the remove the reference from the node. If we are deleting the head or tail — then we just update the respective pointer.

![deleting a node from a linked list](../resources/delete-linked.jpg)

## Usage

Linked lists are dynamic, or flexible in nature. They allow for easy insertion and deletion of nodes[^4] especially at the head and tail. Unlike static arrays, memory does not have to be reallocated if you go over a certain number of nodes. The greatest disadvantage is that it takes O(n) time to traverse a linked list. So operations that take place in the middle of the list can be expensive.

## Time Complexity[^5]

|     Operation      | Description                                        | Time Complexity |
| :----------------: | :------------------------------------------------- | :-------------: |
| insert_head(value) | Inserts value before the head.                     |      O(1)       |
| insert_tail(value) | Inserts value before the head.                     |      O(1)       |
|  insert(i, value)  | Inserts value after position i                     |      O(n)       |
|   remove_head()    | Removes the head                                   |      O(1)       |
|   remove_tail()    | Removes the tail                                   |      O(1)       |
|     remove(i)      | Removes node i                                     |      O(n)       |
|       size()       | Returns the size of the linked list.               |      O(1)       |
|      empty()       | Returns true if the length of the linked list is 0 |      O(1)       |

## Example

## Practice Problem

```python

```

You can find the solution [here](solution.py).

### Footnotes

[^1]: (Brainy Quote)[https://www.brainyquote.com/quotes/herbert_a_simon_193212]
[^2]: How do you explain linked lists in layman's terms?, (Quora)[https://qr.ae/pvPxqO]
[^3]: Linked List, (Wikipedia)[https://en.wikipedia.org/wiki/Linked_list]
[^4]: Under what circumstances are linked lists useful?, (Stack OverFlow)[https://stackoverflow.com/a/2429320]
[^5]: Linked List in Python, (BYU-I CSE)[https://byui-cse.github.io/cse212-course/lesson07/07-prepare.html#1.5]
