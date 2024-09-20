# You are given N elements and your task is to Implement a Stack in which you can get a minimum element.

# Input:
# push(2)
# push(3)
# pop()
# getMin()
# push(1)
# getMin()

# Output:
# 2 1

# Explanation:
# In the first test case for query
# push(2) Insert 2 into the stack.
# The stack will be [2]

# push(3) Insert 3 into the stack.
# The stack will be [2 3]

# pop() Remove top element from stack
# Popped element will be 3
# the stack will be [2]

# getMin() Return the minimum element
# min element will be 2

# push(1) Insert 1 into the stack.
# The stack will be [2 1]

# getMin() Return the minimum element
# min element will be 1

class Solution:
    def __init__(self):
        self.minEle = None
        self.s = []
        self.minstack = []
    
    def getMin(self):
        if not self.minstack:
            return -1
        return self.minstack[-1]
           
    def pop(self):
        if not self.s:
            return -1
        if self.minstack[-1] == self.s[-1]:
            self.minstack.pop()
        return self.s.pop()
       
    def push(self, x):
        self.s.append(x)
        if not self.minstack or self.minstack[-1] >= x:
            self.minstack.append(x)

q = int(input())
ob = Solution()
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        ob.push(query[1])
    elif query[0] == 2:
        print(ob.pop(), end=' ')
    elif query[0] == 3:
        print(ob.getMin(), end=' ')


