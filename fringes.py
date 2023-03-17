class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items = sorted(self.items, key=lambda x: x[1])

    def dequeue(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        return self.items.pop(0)[0]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str([x[0] for x in self.items])
