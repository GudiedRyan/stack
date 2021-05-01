from main import Stack

def test_add():
    test_stack = Stack()
    assert test_stack.add(4) == [4]

def test_is_empty():
    test_stack = Stack()
    assert test_stack.is_empty() == True

def test_is_not_empty():
    test_stack = Stack()
    test_stack.add(5)
    assert test_stack.is_empty() == False

def test_pop():
    stack = Stack()
    stack.add(6)
    stack.add(33)
    assert stack.pop_from_stack() == [6]

def test_empty_pop():
    stack = Stack()
    assert stack.pop_from_stack() == False

def test_peek():
    stack = Stack()
    stack.add(5)
    stack.add(234)
    assert stack.peek() == 234

def test_peek_fail():
    stack = Stack()
    assert stack.peek() == False

def test_sum():
    stack = Stack()
    stack.add(2)
    stack.add(54)
    assert stack.sum_stack() == 56