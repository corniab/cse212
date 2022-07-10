"""
We will create a stack by inheriting from python's built in list.
In addition we will add methods to push and pop.
And we will use the @property decora
"""
class Stack(list):
    def __init__(self):
        # Call the super class constructor.
        super().__init__()
        self._size = 0

    def push(self, value):
        """Adds value to end of the stack."""
        # Call the super class method append.
        super().append(value)

        # Increment the size of the stack.
        self._size += 1

    def pop(self):
        """Removes and returns last value of stack."""
        if not self.empty:            
            # Decrement the size of the stack.
            self._size -= 1

            # Return the return value of the super class method pop.
            return super().pop()

    def clear(self) -> None:
        """Empties the stack of all values."""
        self._size = 0
        return super().clear()

    @property
    def size(self):
        """Returns the size of the stack."""
        return self._size    

    @property
    def empty(self):
        """
        Returns true if size is less than 1.
        Otherwise returns false.
        """
        if self._size < 1:
            return True
        return False

# Create an instance of the Stack
stack = Stack()

# Print instructions to the user
print()
print("+------------------------------------------+")
print("|                                          |")
print("|  This is a simple text editor!           |")
print("|                                          |")
print("|  Type '.q' to quit.                    |")
print("|  Type '.u' to undo previous command.   |")
print("|                                          |")
print("|  Type anything to begin and press enter. |")
print("|                                          |")
print("+------------------------------------------+")
print()

# Prompt the user for input until they type exit
prompt = ""
while prompt != ".q":
    prompt = input("> ")
    if prompt == ".u":
        stack.pop()
        print(" ".join(stack))
        continue
    stack.push(prompt)
    print(" ".join(stack))