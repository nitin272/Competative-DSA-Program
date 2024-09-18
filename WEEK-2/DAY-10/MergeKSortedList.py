class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists: return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            merged.append(merge(lists[i], lists[i+1] if i + 1 < len(lists) else None))
        lists = merged
    return lists[0]

def merge(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

def printList(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

def createLinkedList(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


k = int(input("Enter number of linked lists: "))
lists = []
for i in range(k):
    vals = list(map(int, input(f"Enter sorted elements of list {i+1} (space-separated): ").split()))
    lists.append(createLinkedList(vals))
    
merged_list = mergeKLists(lists)
print("Merged list: ", end="")
printList(merged_list)
