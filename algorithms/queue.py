"""This script implements a queue in Python 3."""


class Queue:
    """
        A class used to represent a queue

        ...

        Attributes
        ----------
        front : int
            a variable that points to the front of the queue
        rear : int
            a variable that points to the back of the queue
        max_size : int
            the largest the queue can be
        """

    def __init__(self):
        self.front = 0
        self.rear = -1
        self.max_size = 10
        self.my_queue = [None] * self.max_size

    def is_empty(self):
        """Checks if there are no items in the queue."""
        return bool(self.front < 0 or self.front > self.rear)

    def is_full(self):
        """Checks if the all the spaces in the queue are filled."""
        return bool(self.rear == self.max_size)

    def size(self):
        """Returns the size of the queue."""
        return len(self.my_queue)

    def enqueue(self, data):
        """Inserts a new item into the queue.

        Parameters
        ----------
        data : int
            The new item to be inserted
        """
        if self.is_full():
            print("Cannot add item to a full queue.")
            return -1
        else:
            self.rear = self.rear + 1
            self.my_queue[self.rear] = data
            return 0

    def dequeue(self):
        """Deletes an item from the queue.
        Returns
        -------
        data : int
            The deleted item
        """
        if self.is_empty():
            print("Cannot delete from an empty queue.")
            return -1
        else:
            data = self.my_queue[self.front]
            self.front = self.front + 1
            return data

    def peek(self):
        """Returns the item at the front of the queue."""
        if self.is_empty():
            print("Cannot peek from an empty queue.")
            return -1
        else:
            return self.my_queue[self.front]


if __name__ == '__main__':
    my_queue = Queue()
    print("Item at front of queue: ", my_queue.peek())
    count = int(input("How many items do you want to add? "))
    for i in range(count):
        number = int(input("Enter a number: "))
        my_queue.enqueue(number)
    print("Item at front of queue: ", my_queue.peek())
    print("Item removed from queue: ", my_queue.dequeue())
    print("Item at front of queue: ", my_queue.peek())
