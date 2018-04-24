from queue import Queue


class MyQueue(Queue):
    """
    MyQueue class for saving nodes and search them in O(1)
    """
    def _init(self, maxsize):
        self.queue = set()

    def _put(self, item):
        self.queue.add(item)

    def _get(self):
        return self.queue.pop()

    def __contains__(self, item):
        return item in self.queue

    def add_all(self, *items):
        for item in items:
            self.queue.add(item)
