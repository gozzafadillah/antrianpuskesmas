from facade.queue_facade import QueueFacade

def Main():
    queue_facade = QueueFacade()

    # Menambahkan beberapa pasien ke antrian
    queue_facade.add_patient("John")
    queue_facade.add_patient("Alice")

    # Menghapus pasien dari antrian
    queue_facade.remove_patient("John")

    # Mendapatkan pasien selanjutnya dari antrian
    next_patient = queue_facade.get_next_patient()
    print("Next patient:", next_patient)

if __name__ == "__main__":
    Main()
