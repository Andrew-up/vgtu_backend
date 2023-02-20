from repository.HealingHistoryRepository import HealingHistoryRepository

class HealingHistoryService(object):
    def __init__(self, doctor_id):
        self.doctor = doctor_id

    def getAllHistoryByIdPatient(self, id_patient):
        h = HealingHistoryRepository(self.doctor)
        return h.getAllHistoryByPatientId(id_patient)


if __name__ == '__main__':
    p = HealingHistoryService(1)
    p.getAllHistoryByIdPatient(5)
    # p2 = PatientDTO()
    # p.getAll()
    # p2.firstname = 'Тест'
    # p.add(p2)

    pass
