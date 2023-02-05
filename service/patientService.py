from repository.PatientRepository import PatientRepository
from model.model import Patient_model_back
from dto.patientDTO import PatientDTO, getPatientDTO_list, getPatient, getPatientDTO

class PatientService(object):

    def __init__(self, doctor_id):
        self.doctor = doctor_id

    def getById(self, item_id) -> Patient_model_back:
        repo = PatientRepository(self.doctor)
        dto = getPatientDTO(repo.get(item_id))
        return dto

    def getAll(self) -> list[PatientDTO]:
        repo = PatientRepository(self.doctor)
        listg = repo.find_all()
        listdto = getPatientDTO_list(listg)
        return listdto

    def add(self, patient_dto: PatientDTO):

        patient: Patient_model_back = getPatient(patient_dto)
        repo = PatientRepository(self.doctor)
        new_patient = repo.add(patient)
        patient_new_DTO = getPatientDTO(new_patient)

        return patient_new_DTO

    def deletePatientById(self, id_patient):
        repo = PatientRepository(self.doctor)
        result_delete = repo.delete_by_id(id_patient=id_patient)
        return result_delete


if __name__ == '__main__':
    p = PatientService(1)
    p2 = PatientDTO()
    p.getAll()
    # p2.firstname = 'Тест'
    p.add(p2)

    pass
