class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(head, x):
    new_node = Node(x)
    new_node.next = head
    head = new_node
    return head

def search_linked_list(head, x):
    current = head
    while current is not None:
        if current.data == x:
            return True
        current = current.next
    return False

head = None
n = int(input())
arr = list(map(int, input().split()))[:n]
for i in range(n):
    head = insert(head, arr[i])

x = int(input())
if search_linked_list(head, x):
    print("true")
else:
    print("false")
