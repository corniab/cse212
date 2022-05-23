# Week 06 Notes

A map uses a set as to store key values. Values are not necessarily unique.

The performace of a map is the same for a set.

Maps are commonly called hashmaps or hashtables.

Python uses dictionaries instead of maps to store values.

```python
# The tutorial overloads the operators '[]' for setting and getting values.

class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()

t["march 6"] = 130
t["march 7"] = 150
t["march 8"] = 160

del t["march 6"]

```

## Resources

- [Hash Table, codebasics](https://www.youtube.com/watch?v=ea8BRGxGmlA)
- [Collision Handling, codebasics](https://www.youtube.com/watch?v=54iv1si4YCM)

## Map Operations

| Operation       | Description                                                     | Performance |
| :-------------- | :-------------------------------------------------------------- | :---------: |
| put(key, value) | Adds or replaces a row in the map withe specified key and value |    O(1)     |
| get(key)        | Gets the value for the specified key                            |    O(1)     |
| remove(key)     | Removes the row from the map containing the specified key.      |    O(1)     |
| member(key)     | Determines if "key" is in the map                               |    O(1)     |
| size()          | Returns the number of items in the map                          |    O(1)     |

## Definitions

- JSON: JavaScript Object Notation. A format used frequently to share data between software. JSON data uses maps and lists. The syntax of JSON is the same as Python.
- key: The keys in the map form a set. EAch key is unique. Keys are used to lookup value form the map.
- map: A data structure that is based on the set. In addition to storing the unique values in the set, the map also includes a value associated with each key. The map has the same O(1) behavior as the set
- value: The value associated with each key within a map. Frequently, these values are referred to as key-value pairs.
