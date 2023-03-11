from LinkedList import ListNode
from LinkedList import List


class Stack:
    def __init__(self):
        self.list = List()

    def push(self, val):
        node = ListNode(val)
        node.next = self.list.head
        self.list.head = node
        self.list.size += 1

    def pop(self):
        if self.list.head == None:
            return None
        else:
            val = self.list.head.val
            self.list.head = self.list.head.next
            self.list.size -= 1
            return val
