from queues.queue import Queue

class QueueDecorator(Queue):
    def __init__(self, queue):
        self.queue = queue

    def add(self, patient):
        # Default implementation, tidak ada perubahan pada antrian dasar
        self.queue.add(patient)

    def remove(self, patient):
        # Default implementation, tidak ada perubahan pada antrian dasar
        self.queue.remove(patient)

    def get_next_patient(self):
        return self.queue.get_next_patient()
