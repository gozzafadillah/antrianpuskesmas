from decorators.queue_decorator import QueueDecorator

class PriorityDecorator(QueueDecorator):
    def add(self, patient):
        # Implementasi untuk menambahkan pasien dengan prioritas
        # (misalnya, memprioritaskan pasien berdasarkan kondisi medis)
        print("Adding patient with priority:", patient.get_name())
        self.queue.add(patient)
