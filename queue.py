
class Queue:
    queue = []
    visited = []

    def __init__(self):
        pass

    def add_to_queue(self, item):
        self.queue.append(item)

    def get_first(self):
        return self.queue[0]

    def pop_first(self):
        self.queue.pop(0)

    def is_not_empty(self):
        if len(self.queue) > 0:
            return True
        else:
            return False

    def list_queue(self):
        return self.queue

