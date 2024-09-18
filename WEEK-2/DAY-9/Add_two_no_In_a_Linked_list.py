class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def print_list(self):
        self._print_list(self.head)
        print()

    def _print_list(self, node):
        if node:
            self._print_list(node.next)
            print(node.data, end=" ")

def addition(num1, num2):
    dummy = Node(0)
    temp, carry = dummy, 0

    while num1 or num2 or carry:
        num1_val = num1.data if num1 else 0
        num2_val = num2.data if num2 else 0
        total = carry + num1_val + num2_val
        carry, value = divmod(total, 10)
        temp.next = Node(value)
        temp = temp.next
        num1 = num1.next if num1 else None
        num2 = num2.next if num2 else None

    return dummy.next

def create_linked_list(data_list):
    llist = LinkedList()
    for data in reversed(data_list):
        llist.insert(data)
    return llist

n1 = int(input())
arr1 = list(map(int, input().split()))[:n1]
llist1 = create_linked_list(arr1)

n2 = int(input())
arr2 = list(map(int, input().split()))[:n2]
llist2 = create_linked_list(arr2)

result = LinkedList()
result.head = addition(llist1.head, llist2.head)
result.print_list()
