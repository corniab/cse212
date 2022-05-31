class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

class Singly_No_Tail:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        """
        Since it has no tail pointer, then you must
        traverse to the end of the list to add a new node.
        """
        if self.head == None:
            self.head = Node(val, self.head)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(val, None)

    def __str__(self) -> str:
        repr_str = "HEAD"
        curr = self.head
        while curr != None:            
            repr_str += " -> " + str(curr.val) 
            curr = curr.next
        return repr_str + " -> NONE"

        

linked_list = Singly_No_Tail()

linked_list.append(10)
linked_list.append(20)
linked_list.append(5)

print(linked_list)