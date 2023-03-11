class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):

        if self.head is None:
            self.head = ListNode(val)
        else:
            node = self.head
            while node is not None:
                node = node.next
            node.next = ListNode(val)
            self.size += 1

    def getListHead(self):
        return self.head

    def getNextNode(self, node):
        return node.next

    def getLastNode(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node
