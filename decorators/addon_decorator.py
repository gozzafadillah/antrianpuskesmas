from decorators.queue_decorator import QueueDecorator

class AddonDecorator(QueueDecorator):
    def add(self, patient):
        # Implementasi untuk menambahkan pasien dengan fitur tambahan
        # (misalnya, menambahkan catatan khusus untuk pasien)
        print("Adding patient with addon:", patient.get_name())
        self.queue.add(patient)
