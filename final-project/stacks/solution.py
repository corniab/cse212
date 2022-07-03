from stack import Stack

class Web_Browser():
    """Class to represent a web browser"""
    def __init__(self) -> None:
        self.current_page = "Home Page"
        self.visited = Stack()
        self.forward = Stack()

        print(self.current_page)

    def visit_page(self, url):
        """Prints the url and adds it to the visited stack."""
        # Clear the forward stack
        self.forward.clear()

        # Add the current page to the visited stack.
        self.visited.push(self.current_page)

        # Update the current page.
        self.current_page = url
        print(self.current_page)

    def go_back(self):
        """Prints the previous page url."""
        # Check if visited stack is not empty
        if self.visited.empty:
            print("Can't go back.")
        else:
            # Add the current page to the forward stack.
            self.forward.push(self.current_page)

            # Update the current page
            self.current_page = self.visited.pop()

            print(self.current_page)

    def go_forward(self):
        if self.forward.empty:
            print("Can't go forward.")
        else:
            # Add the current page to the visited stack
            self.visited.push(self.current_page)

            # Update the current page
            self.current_page = self.forward.pop()

            print(self.current_page)

browser = Web_Browser()

print("Visit some pages")
browser.visit_page("google.com")
browser.visit_page("lds.org")
browser.visit_page("youtube.com")

print()
print("Go back to home page")
browser.go_back()
browser.go_back()
browser.go_back()

print()
print("Go Forward several pages")
browser.go_forward()
browser.go_forward()

print("Visit a new page")
browser.visit_page("reddit.com")
browser.go_forward()
