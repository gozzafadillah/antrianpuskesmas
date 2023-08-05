class Queue:
    def __init__(self):
        self.patients = []

    def add(self, patient):
        self.patients.append(patient)

    def remove(self, patient):
        self.patients.remove(patient)

    def get_next_patient(self):
        if self.patients:
            return self.patients[0]
        return None
