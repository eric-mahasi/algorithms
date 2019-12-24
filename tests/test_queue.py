import unittest

from algorithms import queue


class TestQueue(unittest.TestCase):
    def test_queue_size_on_create(self):
        q = queue.Queue()
        self.assertEqual(q.max_size, q.size())

    def test_is_empty_on_create(self):
        q = queue.Queue()
        for i in range(q.size()):
            self.assertEqual(q.my_queue[i], None)

    def test_enqueue3_dequeue1(self):
        q = queue.Queue()
        q.enqueue(45)
        q.enqueue(9)
        q.enqueue(4)
        self.assertEqual(45, q.dequeue())

    def test_enqueue3_dequeue2(self):
        q = queue.Queue()
        q.enqueue(6)
        q.enqueue(5)
        q.enqueue(7)
        q.dequeue()
        self.assertEqual(5, q.dequeue())

    def test_peek_empty(self):
        q = queue.Queue()
        self.assertEqual(-1, q.peek())

    def test_dequeue_empty(self):
        q = queue.Queue()
        self.assertEqual(-1, q.dequeue())

    def test_enqueue_dequeue1(self):
        q = queue.Queue()
        q.enqueue(20)
        self.assertEqual(20, q.dequeue())


if __name__ == '__main__':
    unittest.main()
