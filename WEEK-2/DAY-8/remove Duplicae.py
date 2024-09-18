class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head
    while current:
        while current.next and current.data == current.next.data:
            current.next = current.next.next
        current = current.next
    return head

def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.data))
        current = current.next
    print(' '.join(result))

def create_linked_list(values):
    if not values:
        return None
    head = Node(int(values[0]))
    current = head
    for value in values[1:]:
        new_node = Node(int(value))
        current.next = new_node
        current = new_node
    return head

input_string = input("Enter space-separated integers: ")


values = input_string.split()
head = create_linked_list(values)

head = remove_duplicates(head)


print_linked_list(head)
