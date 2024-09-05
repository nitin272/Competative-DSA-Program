class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next


values = list(map(int, input("Enter the values for the linked list (space-separated): ").split()))
n = int(input("Enter the value of n: "))
head = build_linked_list(values)

new_head = removeNthFromEnd(head, n)

print("Linked list after removal:")
print_linked_list(new_head)
