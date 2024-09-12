
class Node:
  def __init__(self,data):
    self.data =data
    self.next = None

def create_(values):
  if not values:
    return None
  head = Node(values[0])
  current = head
  for value in values[1:]:
    current.next = Node(value)
    current = current.next
  return head

def find_middle(head):
  if not head:
    return None
  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow


size = int(input())
values= list(map(int,input().split()))


head= create_(values)
middle= find_middle(head)
print(middle.data)