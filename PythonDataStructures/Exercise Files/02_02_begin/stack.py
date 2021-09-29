"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    # Constructor
    def __init__(self):
        self.items = []  # The items property of the instance we are talking about

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items  # An empty list evaluates as false

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]  # Gets the item at the end of the list

    def size(self):
        return len(self.items)

    # Use print statement to inspect stack
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())
