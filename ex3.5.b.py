import random
import timeit
import time
import matplotlib.pyplot as plt

# heap implementaion is effecient priority queue

# both the datastructers are modefied so that they can hold the time values

# LinkedList is ineffecinat priority queue implementation


class Node:
    def __init__(self, data=None, priority=None):
        self.data = data
        self.priority = priority
        self.next = None


class ListPriorityQueue:
    def __init__(self):
        self.head = None
        self.listInsertTime = []
        self.listpopTime = []

    def insert(self, data):
        start_time = time.time()

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        elif self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next

            new_node.next = current.next
            current.next = new_node

        end_time = time.time()
        elapsed_time = end_time - start_time

        self.listInsertTime.append(elapsed_time)

    def get_min(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def extract_min(self):
        start_time = time.time()

        if self.head is None:
            return None

        min_node = self.head
        self.head = self.head.next

        end_time = time.time()
        elapsed_time = end_time - start_time

        self.listpopTime.append(elapsed_time)

        return min_node.data

    def getInsertTime(self):
        return self.listInsertTime

    def getPopTime(self):
        return self.listpopTime

# the following is a priorityQueue datastructer implemented with a heap
# heaps are elegent for the fact that the data is very compact
# we do not need to recursivly define a binary tree datastructer
# instead we store data in an array


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.listInsertTime = []
        self.listpopTime = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        start_time = time.time()
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.listInsertTime.append(elapsed_time)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def get_min(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]

    def extract_min(self):
        start_time = time.time()

        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.listpopTime.append(elapsed_time)

        return root

    def heapify_down(self, i):
        min_index = i

        left = self.left_child(i)
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        right = self.right_child(i)
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if i != min_index:
            self.swap(i, min_index)
            self.heapify_down(min_index)

    def getInsertTime(self):
        return self.listInsertTime

    def getPopTime(self):
        return self.listpopTime


def graphData(listInsertTime, listPopTime, heapInsertTime, heapPopTime):
    xPoints = [i for i in range(len(listInsertTime))]

    plt.subplot(2, 2, 1)
    plt.plot(xPoints, listInsertTime)
    plt.title("LinkedList Insertion time")
    plt.xlabel('iteration number')
    plt.ylabel('function call speed')

    plt.subplot(2, 2, 2)
    plt.plot(xPoints, listPopTime)
    plt.title("LinkedList pop time")
    plt.xlabel('iteration number')
    plt.ylabel('function call speed')

    plt.subplot(2, 2, 3)
    plt.plot(xPoints, heapInsertTime)
    plt.title("Heap Insertion time")
    plt.xlabel('iteration number')
    plt.ylabel('function call speed')

    plt.subplot(2, 2, 4)
    plt.plot(xPoints, heapPopTime)
    plt.title("Heap pop time")
    plt.xlabel('iteration number')
    plt.ylabel('function call speed')

    plt.show()


if __name__ == "__main__":

    listQueue = ListPriorityQueue()

    for i in range(1000):
        randomInt = random.randint(-100, 100)
        listQueue.insert(randomInt)
    listInsertTime = listQueue.getInsertTime()
    for i in range(1000):
        listQueue.extract_min()
    listPopTime = listQueue.getPopTime()

    heapQueue = PriorityQueue()
    for i in range(1000):
        randomInt = random.randint(-100, 100)
        heapQueue.insert(randomInt)
    heapInsertTime = heapQueue.getInsertTime()
    for i in range(1000):
        heapQueue.extract_min()
    heapPopTime = heapQueue.getPopTime()

    graphData(listInsertTime, listPopTime, heapInsertTime, heapPopTime)
