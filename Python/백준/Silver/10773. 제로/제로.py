class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
n = int(input())
stack = Stack()
for i in range(n):
    n2 = int(input())
    if n2 == 0:
        stack.pop()
    else:
        stack.push(n2)
print(sum(stack.stack))