class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

def loopHere(head, tail, position):
    if position == 0:
        return
    
    walk = head
    for i in range(1, position):
        walk = walk.next

    tail.next = walk 

def detectLoop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

n = int(input()) 

arr = list(map(int, input().split()))[:n] 

num = arr[0]
head = tail = Node(num)

for i in range(1, n):  
    tail.next = Node(arr[i])
    tail = tail.next

pos = int(input())  
loopHere(head, tail, pos)  

ans = detectLoop(head) 
if ans:
    print("True")
else:
    print("False")
