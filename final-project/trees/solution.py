class Node:
    def __init__(self, data, id=""):
        """Creates an instance of a node."""
        self.data = data
        self.parent = None
        self.children = []
        self.id = id

    def append_child(self, node: "Node"):
        """Adds a child node."""
        node.parent = self
        self.children.append(node)
    
    @property
    def height(self) -> int:
        """Get the height of the node."""
        node = self
        level = 0 
        while node.parent != None:
            level += 1
            node = node.parent
        return level

    def __str__(self) -> str:
        """Creates a string representation of a Node."""
        str_val = ""
        str_val += f"\nTag:        {self.data}"
        str_val += f"\nParent:     {self.parent.data}"
        str_val += f"\nChildren:   {', '.join(child.data for child in self.children)}"
        str_val += f"\nId:         {self.id}"

        return str_val

class DocumentTree(Node):
    def __init__(self):
        """Creates a document tree whose root node is DOCUMENT."""
        # Constructor for super class.
        super().__init__(self)

        # Set the data of the root node to be 
        self.data = "DOCUMENT"

    def create_element(self, data, id=""):
        """Create a new node."""
        return Node(data, id)

    def get_element_by_id(self, id): 
        """
        Gets first node with id.
        Performance: O(n).
        """
        return self._get_element_by_id(id, self)            

    def _get_element_by_id(self, id, node: Node):
        """Searches for selector name."""

        # If the selector is present in the node's selectors
        # Then return the current node.
        if id == node.id:
            return node
        
        # Base Case: We have reached a leaf.
        if len(node.children) < 1:
            return None

        # Continue searching tree.
        else:            
            for child in node.children:
                result = self._get_element_by_id(id, child)
                
                # Return result if we found a matching node.
                if result is not None: 
                    return result

        # We did not find a matching node.
        return None

    def remove_element_by_id(self, id):
        """Removes first element with id."""

        return self._remove_element_by_id(id, self)

    def _remove_element_by_id(self, id, node: Node, i=0):
        """Removes an element and all child nodes by id."""
        # If the selector is present in the node's selectors
        # Then return the current node.
        if id == node.id:
            del node.parent.children[i]
            return (node, i)
        
        # Base Case: We have reached a leaf.
        if len(node.children) < 1:
            return None

        # Continue searching tree.
        else:            
            for i, child in enumerate(node.children):
                result = self._remove_element_by_id(id, child, i)
                
                # Return result if we found a matching node.
                if result is not None:
                    return result

        # We did not find a matching node.
        return None

    def __str__(self) -> str:
        """Print a string representation of Document Tree"""
        return self._str(self)

    def _str(self, node: Node, line=""):
        """Build string line by line"""
        # If we start with the parent node then we just need its data.
        if node.parent == None:
            line = node.data

        # Create a new, indented line for each node.
        else:
            indent = " " * node.height * 4 + "|__"
            line = "\n" + indent + node.data 
    
        # Base Case: We have reached a leaf.
        if len(node.children) < 1:
            return line
        
        # Create a new line for each child node.
        for child in node.children:
           line += self._str(child)

        # Return the final string from each subtree.
        return line



# Create new instance of document tree.
document = DocumentTree()

document.id = "#document"

# Create html element.
html = document.create_element("HTML")

# Create head element.
head = document.create_element("HEAD")

# Create a head element.
title = document.create_element("TITLE")

# Create body element.
body = document.create_element("BODY")

# Create main element.
main = document.create_element("MAIN", "#main")

# Create header element.
header = document.create_element("HEADER")

# Create a section element.
section = document.create_element("SECTION")

# Create a footer element.
footer = document.create_element("FOOTER")

# Append children.
document.append_child(html)
html.append_child(head)
html.append_child(body)
head.append_child(title)
body.append_child(main)
main.append_child(header)
main.append_child(section)
main.append_child(footer)

print(document)
"""
Output should look like the following:

DOCUMENT
    |__HTML
        |__HEAD     
            |__TITLE
        |__BODY
            |__MAIN
                |__HEADER
                |__SECTION
                |__FOOTER
"""

print(document.remove_element_by_id("#main"))
print(document)
"""
Output should look like the following:

DOCUMENT
    |__HTML
        |__HEAD     
            |__TITLE
        |__BODY
"""