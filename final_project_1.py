class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def sorted_merge(self, other_list):
        p = self.head
        q = other_list.head
        sorted_list = SinglyLinkedList()

        while p and q:
            if p.data <= q.data:
                sorted_list.append(p.data)
                p = p.next
            else:
                sorted_list.append(q.data)
                q = q.next

        while p:
            sorted_list.append(p.data)
            p = p.next

        while q:
            sorted_list.append(q.data)
            q = q.next

        return sorted_list

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self

        mid = self.get_middle()
        left_half = SinglyLinkedList()
        right_half = SinglyLinkedList()
        left_half.head = self.head
        right_half.head = mid.next
        mid.next = None

        left_sorted = left_half.merge_sort()
        right_sorted = right_half.merge_sort()

        sorted_list = left_sorted.sorted_merge(right_sorted)
        return sorted_list

    def get_middle(self):
        if self.head is None:
            return self.head

        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    # Створення однозв'язного списку та додавання елементів
singly_linked_list = SinglyLinkedList()
singly_linked_list.append(3)
singly_linked_list.append(1)
singly_linked_list.append(5)
singly_linked_list.append(2)
singly_linked_list.append(4)

print("Original List:")
singly_linked_list.print_list()

# Реверс списку
singly_linked_list.reverse()
print("Reversed List:")
singly_linked_list.print_list()

# Сортування списку за допомогою сортування злиттям
sorted_list = singly_linked_list.merge_sort()
print("Sorted List:")
sorted_list.print_list()

# Об'єднання двох відсортованих списків
list1 = SinglyLinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = SinglyLinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = list1.sorted_merge(list2)
print("Merged Sorted List:")
merged_list.print_list()

