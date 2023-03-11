import threading
import random
import time


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        self.lock()
        insertPos = (self.head + 1) % self.size
        if insertPos != self.tail:  # if queue is not full simply insert element
            self.queue[insertPos] = data
            self.head += 1
            self.unlock()
            return
        else:  # if its full wait 1 second then add the element
            time.sleep(1)
            self.enqueue(data)

    def dequeue(self):
        self.lock()
        dequeuePos = (self.tail + 1) % self.size
        if dequeuePos != self.head:
            self.queue[dequeuePos] = None
            self.tail += 1
            self.unlock()
            return
        else:
            time.sleep(1)
            self.dequeue()


def producer():
    queue = CircularQueue(30)
    while True:
        random_number = random.randint(1, 10)
        time.sleep(random_number)
        queue.enqueue(random_number)


def consumer():
    queue = CircularQueue(30)
    while True:
        random_number = random.randint(1, 10)
        time.sleep(random_number)
        queue.dequeue(random_number)


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
