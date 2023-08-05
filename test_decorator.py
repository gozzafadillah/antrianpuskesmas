import unittest
from queues.queue import Queue
from decorators.priority_decorator import PriorityDecorator
from decorators.addon_decorator import AddonDecorator
from queues.patient import Patient

class TestDecorator(unittest.TestCase):
    def test_priority_decorator(self):
        queue = Queue()
        priority_queue = PriorityDecorator(queue)

        patient1 = Patient("John")
        patient2 = Patient("Jane")

        priority_queue.add(patient1)
        queue.add(patient2)

        next_patient = priority_queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "John")
        
        next_patient = queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "Jane")

    def test_addon_decorator(self):
        queue = Queue()
        addon_queue = AddonDecorator(queue)

        patient1 = Patient("John")
        patient2 = Patient("Jane")

        queue.add(patient1)
        addon_queue.add(patient2)

        next_patient = addon_queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "Jane")
        
        next_patient = queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "John")

if __name__ == '__main__':
    unittest.main()
