def init(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def extract_max(self):
        if len(self.queue) == 0:
            return None
        max_val = max(self.queue)
        self.queue.remove(max_val)
        return max_val

class PriorityQueue:
    def init(self):
        self.queue = []

    def insert(self, value):
        heapq.heappush(self)