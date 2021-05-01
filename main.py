class Stack:

    def __init__(self):
        self.stack = []
    
    def add(self, number: int):
        self.stack.append(number)
        return self.stack
    
    def is_empty(self):
        return len(self.stack) == 0

    def pop_from_stack(self):
        try:
            self.stack.pop()
            return self.stack
        except:
            return False
    
    def peek(self):
        try:
            return self.stack[-1]
        except:
            return False

    def sum_stack(self):
        return sum(self.stack)