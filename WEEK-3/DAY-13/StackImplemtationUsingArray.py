class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
    
    def push(self, element):
        if len(self.stack) == self.max_size:
            print("stack overflow")
        else:
            self.stack.append(element)
    
    def pop(self):
        if len(self.stack) == 0:
            print("stack underflow")
        else:
            return self.stack.pop()
    
    def top(self):
        if len(self.stack) == 0:
            print("stack underflow")
        else:
            return self.stack[-1]

test_cases = int(input())

for _ in range(test_cases):
    n, s = map(int, input().split())
    stack = Stack(s)
    
    for _ in range(n):
        command = input().split()
        
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            popped = stack.pop()
            if popped is not None:
                print(popped)
        elif command[0] == "top":
            top = stack.top()
            if top is not None:
                print(top)
