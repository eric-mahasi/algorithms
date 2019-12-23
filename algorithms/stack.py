"""This script implements a stack in Python 3."""


class Stack:
    """
    A class used to represent a stack

    ...

    Attributes
    ----------
    top : int
        a variable that points to the of the top of the stack
    max_size : int
        the largest the stack can be
    """
    def __init__(self):
        self.top = 0
        self.max_size = 10
        self.my_stack = [None] * self.max_size

    def is_full(self):
        """Checks if the all the spaces in the stack are filled."""
        return bool(self.top == self.max_size)

    def is_empty(self):
        """Checks if there are no items in the stack."""
        return bool(self.top == -1)

    def peek(self):
        """Returns the item at the top of the stack."""
        return self.my_stack[self.top]

    def pop(self):
        """Deletes an item from the stack.
        Returns
        -------
        popped : int
            The deleted item
        """
        if self.is_empty():
            print("Cannot pop from an empty stack.")
            return -1
        else:
            popped = self.my_stack[self.top]
            self.top = self.top - 1
            return popped

    def push(self, data):
        """Inserts a new item into the stack.

        Parameters
        ----------
        data : int
            The new item to be inserted
        """
        if self.is_full():
            print("Cannot push into a full stack.")
            return -1
        else:
            self.top = self.top + 1
            self.my_stack[self.top] = data
            return 0


if __name__ == '__main__':
    my_stack = Stack()
    print("Item at top of stack: ", my_stack.peek())
    count = int(input("How many items do you want to add? "))
    for i in range(count):
        number = int(input("Enter a number: "))
        my_stack.push(number)
    print("Item at top of stack: ", my_stack.peek())
    print("Item popped from stack: ", my_stack.pop())
    print("Item at top of stack: ", my_stack.peek())
