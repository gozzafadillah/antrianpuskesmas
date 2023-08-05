import unittest
from facade.queue_facade import QueueFacade

class TestFacade(unittest.TestCase):
    def test_queue_facade(self):
        queue_facade = QueueFacade()

        queue_facade.add_patient("John")
        queue_facade.add_patient("Jane")
        queue_facade.add_patient("Smith")

        next_patient = queue_facade.get_next_patient()
        self.assertEqual(next_patient, "John")
        
        queue_facade.remove_patient("John")

        next_patient = queue_facade.get_next_patient()
        self.assertEqual(next_patient, "Jane")

if __name__ == '__main__':
    unittest.main()
