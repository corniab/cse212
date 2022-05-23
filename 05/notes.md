# Week 05 Notes

## Sets

Sets are uselful when order is not important
Sets use hashing to store values by index

### Application

- fast performance for adding, removing, and finding
- no duplicates are allowed.
- the order of values is determined by the index hasing function

### Uses

- finding unique values
- providing quick access to unique results
- performing set operations

### Collision Handling

- collisions can be handled using chaining or linear probing
- linear probing searches the list for the next available spot
- chaining appends the value to a linked list available at the index

## Definitions

- chaining: a method of removing conflicts in a set in which all items that hast to the same index are chained together into a single data structure stored in that target indes. When looking for data, the code will need to traverse the data structure.
- hashing: the process of mapping an item to an index location using a hashing function.Since th function does not require searching through the data structure, hashing can result in an O(1) in the best case
- hashing function: a function that converts the value of an item to a numerical index value. The hashing function will includea modulo operation to ensure the reulting index is within range of the sparsed list
- open addressing: a method of removing conflicts in a set in which a new empty locatoin is found elsewhere in the sparse list. There are multiple ways of finding an empty location including moving over 1 index at a time until one is found. When looking for data, the code will need to follow this search strategy until something is found
- set: a data structure that maps data to an index based on a hashing function. Sets can only hold unique data because of the hashing function. Sets are useful for summarizing data and finding duplicates
- sparse list: an array that is only partially filled. to avoid conflicts in a set, a sparse list must have sufficient empty space to allow for new additions. if a sparse list gets too full, a large sparsed list could be created with an updated hashing function.
