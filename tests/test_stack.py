import unittest

from algorithms import stack


class TestStack(unittest.TestCase):
    def test_stack_on_create_size(self):
        s = stack.Stack()
        self.assertEqual(s.max_size, s.size())

    def test_is_empty_on_create(self):
        s = stack.Stack()
        for i in range(s.size()):
            if s.my_stack[i] is None:
                self.assertEqual(s.my_stack[i], None)

    def test_push_3_pop1(self):
        s = stack.Stack()
        s.push(4)
        s.push(6)
        s.push(2)
        self.assertEqual(2, s.pop())

    def test_push_2_pop_2(self):
        s = stack.Stack()
        s.push(4)
        s.push(6)
        s.push(2)
        s.pop()
        self.assertEqual(6, s.pop())

    def test_is_empty_push1(self):
        s = stack.Stack()
        s.push(5)
        self.assertEqual(False, s.is_empty())

    def test_peek_push1(self):
        s = stack.Stack()
        s.push(79)
        self.assertEqual(79, s.peek())

    def test_peek_push3_pop1(self):
        s = stack.Stack()
        s.push(0)
        s.push(48)
        s.push(23)
        s.pop()
        self.assertEqual(48, s.peek())


if __name__ == '__main__':
    unittest.main()
