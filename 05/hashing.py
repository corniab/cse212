from pprint import pp


class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.arr = [[] for _ in range(self.Max)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        for i, el in enumerate(self.arr[h]):
            if len(el) == 2 and el[0] == key:
                self.arr[h][i] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for el in self.arr[h]:
            if el[0] == key:
                return el[1]
        return None
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, el in enumerate(self.arr[h]):
            if el[0] == key:
                del self.arr[h][i]
                break
        return None

t = HashTable()

t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459

pp(t.arr)

del t["march 6"]

pp(t.arr)