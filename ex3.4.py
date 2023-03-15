import threading
import time
import random


class Queue:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.end = 0
        self.count = 0
        self.lock = threading.Lock()
        self.empty = threading.Condition(self.lock)
        self.full = threading.Condition(self.lock)


    def enqueue(self, item):
        while self.count == self.size:
            self.full.wait(1)
        self.lock.acquire()
        if self.count < self.size:
            self.buffer[self.end] = item
            self.end = (self.end + 1) % self.size
            self.count += 1
            self.empty.notify()
        self.lock.release()


    def dequeue(self):
        while self.count == 0:
            self.empty.wait(1)
        self.lock.acquire()
        item = None
        if self.count > 0:
            item = self.buffer[self.start]
            self.start = (self.start + 1) % self.size
            self.count -= 1
            self.full.notify()
        self.lock.release()
        return item


def producer(queue):
    while True:
        num = random.randint(1, 10)
        time.sleep(num)
        queue.enqueue(num)


def consumer(queue):
    while True:
        num = random.randint(1, 10)
        time.sleep(num)
        item = queue.dequeue()
        if item:
            print(item)


if __name__ == '__main__':
    q = Queue(5)
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()