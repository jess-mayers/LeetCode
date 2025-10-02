class LinkedList:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def __next__(self):
        return self.next

    def __str__(self):
        # get remaining items in list
        values = []
        node = self
        while node is not None:
            values.append(node.val)
            node = node.next
        return ', '.join(values)