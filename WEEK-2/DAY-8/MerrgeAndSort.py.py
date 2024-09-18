
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_linked_lists(a, b):
   dummy = Node(0)
   tail = dummy
   
   while a is not None and b is not None:
       if a.data < b.data:
           tail.next = a
           a = a.next
       else:
           tail.next = b
           b = b.next
       tail = tail.next
        
   if a:
       tail.next = a
   else:
       tail.next = b
   return dummy.next
def print_linked_list(node):
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Direct execution starts here
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

list1 = create_linked_list(arr1)
list2 = create_linked_list(arr2)

merged_list = merge_linked_lists(list1, list2)
print("Merged Linked List:")
print_linked_list(merged_list)









