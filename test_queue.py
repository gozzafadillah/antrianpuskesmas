import unittest
from queues.queue import Queue
from queues.patient import Patient

class TestQueue(unittest.TestCase):
    def test_add_and_get_next_patient(self):
        queue = Queue()
        patient1 = Patient("John")
        patient2 = Patient("Jane")

        queue.add(patient1)
        queue.add(patient2)

        next_patient = queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "John")
        
    def test_remove_patient(self):
        queue = Queue()
        patient1 = Patient("John")
        patient2 = Patient("Jane")

        queue.add(patient1)
        queue.add(patient2)

        queue.remove(patient1)

        next_patient = queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "Jane")

if __name__ == '__main__':
    unittest.main()
