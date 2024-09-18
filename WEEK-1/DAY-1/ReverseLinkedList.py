class Node:

    def __init__(self,data):
        self.data  = data
        self.prev = None
        self.next = None


def create_linked_List(values):
    head = None
    prev_node = None
    for value in values:
        node  = Node(value)
        if prev_node:
            prev_node.next = node 
            node.prev = prev_node
        else:
            head = node
        prev_node = node
    return head


def print_linked_list(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next



def reverse_linked_list(head):
   if head is None or head.next is None:
      return head
   
   current = head
   new_head = None
   while current is not None:
      next_node = current.next
      current.next = current.prev
      current.prev = next_node
      new_head =current
      current = next_node
   return new_head



values = input("enter elements").split()

head = create_linked_List(values)

head = reverse_linked_list(head)
print_linked_list(head)

    