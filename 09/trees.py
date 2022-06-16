class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self, node):
        level = 0 
        while node.parent != None:
            level += 1
            node = node.parent
        return level

    def __str__(self, str_val="") -> str:
        # Add parent.
        if self.parent == None:
            str_val = str(self.data)
        # base case
        if len(self.children) < 1:
            return str_val
        for child in self.children:
            indent =  " " * self.get_level(child) * 4 + "|__"
            line = "\n" + indent + str(child.data)
            str_val += child.__str__(line)
        return str_val        

    @staticmethod
    def build_tree():
        president = TreeNode("President")

        ceo = TreeNode("CEO")
        ceo.add_child(TreeNode("Human Resources"))
        ceo.add_child(TreeNode("Logistics"))
        ceo.add_child(TreeNode("Acquisitions"))

        cfo = TreeNode("CFO")
        cfo.add_child(TreeNode("Accounting"))
        cfo.add_child(TreeNode("Sales"))
        cfo.add_child(TreeNode("Marketing"))

        coo = TreeNode("COO")
        coo.add_child(TreeNode("Production"))
        coo.add_child(TreeNode("Shipping"))
        coo.add_child(TreeNode("Fabrication"))

        
        president.add_child(ceo)
        president.add_child(cfo)
        president.add_child(coo)

        return president

bst = TreeNode.build_tree()
print(bst)
