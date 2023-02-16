from model.model import Patient

class PatientDTO(object):

    def __init__(self, **entries):
        self.id_patient = None
        self.firstname = None
        self.last_name = None
        self.middle_name = None
        self.date_of_birth = None
        self.address = None
        self.phone = None
        self.polis_oms = None
        self.snils = None
        self.document = None
        self.gender = None
        self.__dict__.update(entries)

# Передать PatientDTO получить Patient
def getPatient(patient_dto_back: PatientDTO):
    p = Patient()
    p.firstname = patient_dto_back.firstname
    p.surname = patient_dto_back.last_name
    p.middlename = patient_dto_back.middle_name
    p.snils = patient_dto_back.snils
    p.document = patient_dto_back.document
    p.phone = patient_dto_back.phone
    p.date_of_birth = patient_dto_back.date_of_birth
    p.address = patient_dto_back.address
    p.polis_oms = patient_dto_back.polis_oms
    p.gender = patient_dto_back.gender
    return p

# Передать patient_model_back получить PatientDTO
# Пример:
# dto = PatientDTO()
# patient = Patient_model_back()
# res = dto.getPatientDTO(patient)

def getPatientDTO(patient_model_back: Patient):
    p_dto = PatientDTO()
    p_dto.id_patient = patient_model_back.id_patient
    p_dto.firstname = patient_model_back.firstname
    p_dto.last_name = patient_model_back.surname
    p_dto.middle_name = patient_model_back.middlename
    p_dto.snils = patient_model_back.snils
    p_dto.document = patient_model_back.document
    p_dto.date_of_birth = patient_model_back.date_of_birth
    p_dto.gender = patient_model_back.gender
    p_dto.phone = patient_model_back.phone
    p_dto.polis_oms = patient_model_back.polis_oms
    p_dto.address = patient_model_back.address
    return p_dto


def getPatientDTO_list(patient_model_back: list[Patient]) -> list[PatientDTO]:
    dto_list = list[PatientDTO]()
    for i in range(len(patient_model_back)):
        dto = PatientDTO()
        if patient_model_back[i].id_patient is not None:
            dto.id_patient = patient_model_back[i].id_patient
        dto.firstname = patient_model_back[i].firstname
        dto.last_name = patient_model_back[i].surname
        dto.middle_name = patient_model_back[i].middlename
        dto.snils = patient_model_back[i].snils
        dto.document = patient_model_back[i].document
        dto.date_of_birth = patient_model_back[i].date_of_birth
        dto.gender = patient_model_back[i].gender
        dto.phone = patient_model_back[i].phone
        dto.polis_oms = patient_model_back[i].polis_oms
        dto.address = patient_model_back[i].address
        dto_list.append(dto)
    return dto_list
