class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insert(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def delete_first(head):
    if head:
        return head.next
    return None
def display(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
head = None
n = int(input().strip())
arr = list(map(int, input().strip().split()))[:n]
for num in arr:
    head = insert(head, num)

head = delete_first(head)


display(head)
