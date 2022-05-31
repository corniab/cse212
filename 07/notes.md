# Week 07 Notes

### Advantages

- it can grow and shrink at runtime. don't have to declare intial size
- insertion and deletion is easier than in an array. No shifting.
- no memory wastage. allocates memory as needed
- stacks and queues can be easily implented using a linked list
-

### Disadvantages

- requires more memory to store pointer
- traversal is difficult. no access by index.
- reverse traversal requires more memory
  [thecrazyprogrammer.com](https://www.thecrazyprogrammer.com/2016/11/advantages-disadvantages-linked-list.html)

## Common Operations

| Operation             | Description                                        | Performance |
| :-------------------- | :------------------------------------------------- | ----------: |
| insert_head(value)    | Adds "value" before the head                       |        O(1) |
| insert_tail(value)    | Adds "value" after the tail                        |        O(1) |
| insert_head(i, value) | Adds "value" after node "i"                        |        O(n) |
| remove_head()         | Removes the first item (the head)                  |        O(1) |
| remove_tail(index)    | Removes the last item (the tail)                   |        O(1) |
| remove(i)             | Removes node "i"                                   |        O(1) |
| size()                | Return the size of the linked list                 |        O(1) |
| empty()               | Returns true if the length of the linked list is 0 |        O(1) |

## Definitions

- doubly-linked list: a linked list that is bi-directional. Thie linked list will maintain both a head and a tail. To traverse in either direction, the node will have both a pointer to the next node and the previous node. Access to both the head and tail is O(1).
- head: a pointer to the first node in the linked list.
- linked list: a data structure that keeps data in order but is not in contiguous memory. To get to the next (or previous) item in the list, pointers are maintained and followed. Access to the head is O(1).
- next: a pointer in each node of the linked list that points to the next node.
- node: the combination of the value and the pointers representing one item in the linked list.
- pointer: refers to an address in the computer memory. Also called a reference
- tail: a pointer to the last node in the linked list. If the list has only one item, then the head and tail are the same.
- value: the actual data stored in the linked list as part of the node.
- previous: a pointer in each of the linked list nodes that points to the previous node.
