class Node:
    def __init__(self, data, class_name="", id=""):
        """Creates an instance of a node."""
        self.data = data
        self.parent = None
        self.children = []
        self.class_name = class_name
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
        str_val += f"\nClass Name: {self.class_name}"

        return str_val

class DocumentTree(Node):
    def __init__(self):
        """Creates a document tree whose root node is DOCUMENT."""
        # Constructor for super class.
        super().__init__(self)

        # Set the data of the root node to be 
        self.data = "DOCUMENT"

    def create_element(self, data):
        """Create a new node."""
        return Node(data)

    def get_element_by_class_name(self, selector_name): 
        """
        Gets first node with class selector name.
        Performance: O(n).
        """
        return self._get_element_by_class_name(selector_name, self)            

    def _get_element_by_class_name(self, selector_name, node: Node):
        """Searches for selector name."""

        # If the selector is present in the node's selectors
        # Then return the current node.
        if selector_name == node.class_name:
            return node
        
        # Base Case: We have reached a leaf.
        if len(node.children) < 1:
            return None

        # Continue searching tree.
        else:            
            for child in node.children:
                result = self._get_element_by_class_name(selector_name, child)
                
                # Return result if we found a matching node.
                if result is not None: 
                    return result

        # We did not find a matching node.
        return None

    def get_element_by_id(self, id):
        """
        Gets element by id. 
        Performance: O(n).
        """

    def _get_element_by_id(self, id, node: Node):
        """Searches for element with id."""

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

# Create html element.
html = document.create_element("HTML")

# Create head element.
head = document.create_element("HEAD")

# Create a head element.
title = document.create_element("TITLE")

# Create body element.
body = document.create_element("BODY")

# Create main element.
main = document.create_element("MAIN")

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