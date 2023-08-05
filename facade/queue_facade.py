from queues.patient import Patient
from queues.queue import Queue  # Perbaikan disini
from decorators.priority_decorator import PriorityDecorator
from decorators.addon_decorator import AddonDecorator

class QueueFacade:
    def __init__(self):
        # Membuat antrian dasar dan menerapkan decorator
        queue = Queue()
        queue = PriorityDecorator(queue)
        queue = AddonDecorator(queue)
        self.queue = queue

    def add_patient(self, name):
        patient = Patient(name)
        self.queue.add(patient)

    def remove_patient(self, name):
        # Implementasi untuk menghapus pasien berdasarkan nama
        # (misalnya, mencari pasien dengan nama yang sesuai dan menghapusnya dari antrian)
        pass

    def get_next_patient(self):
        patient = self.queue.get_next_patient()
        return patient.get_name() if patient else None
