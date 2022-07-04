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

To insert a node into the middle of a linked list we just update the pointers (references) to the appropriate nodes.

![inserting a node into a linked list](../resources/insert-linked.jpg)

Deleting a node from the middle is similar in fashion to inserting. We just update the pointers and the remove the reference from the node.

![deleting a node from a linked list](../resources/delete-linked.jpg)

## Usage

## Time Complexity

## Example

## Practice Problem

```python

```

You can find the solution [here](solution.py).

### Footnotes

[^1]: (Brainy Quote)[https://www.brainyquote.com/quotes/herbert_a_simon_193212]
[^2]: How do you explain linked lists in layman's terms?, (Quora)[https://qr.ae/pvPxqO]
[^3]: Linked List, (Wikipedia)[https://en.wikipedia.org/wiki/Linked_list]
[^4]: ()[]
[^5]: ()[]
