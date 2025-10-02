class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def __next__(self):
        return self.next

class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        return ' -> '.join(values)

    def append(self, val):
        node = Node(val=val)
        if self.head is None:
            self.head = node
            return

        # add node to end of linked list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def pop(self, index: int = None):
        if self.head is None:
            raise IndexError('Cannot pop from empty list')

        if index is None:
            # remove last element
            if not self.head.next:
                # if head has no next set head to none and return val
                val = self.head.val
                self.head = None
                return val

            current = self.head
            # get second to last node
            while current.next and current.next.next:
                current = current.next
            val = current.next.val
            current.next = None
            return val

        else:
            # remove at index
            if not isinstance(index, int) or index < 0:
                # index must be an int or greater than 0
                raise IndexError('index must be an int greater than 0')

            if index == 0:
                val = self.head.val
                self.head = self.head.next
                return val

            current = self.head
            previous = None
            while current is not None and index > 0:
                previous = current
                current = current.next
                index -= 1

            if current is None:
                raise IndexError('Index out of range')

            val = current.val
            previous.next = current.next
            return val

    def remove(self, index: int):
        self.pop(index)
