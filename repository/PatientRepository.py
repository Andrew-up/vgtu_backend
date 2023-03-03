from sqlalchemy.orm import Session, sessionmaker, joinedload, Load, lazyload
from sqlalchemy import create_engine

from model.model import Patient, HealingHistory, ResultPredict
from repository.abstractRepository import AbstractRepository
from definitions import DATABASE_DIR

engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


class PatientRepository(AbstractRepository):

    def __init__(self, doctor_id):
        self.session = sessionmaker(bind=engine)()
        self.doctor = doctor_id

    def get(self, id_patient) -> Patient:
        self.session.connection()
        get: Patient = self.session.query(Patient).get(id_patient)
        self.session.close()
        return get

    def getFullPatient(self, id_patient) -> Patient:
        self.session.connection()
        # p: Patient = self.session.query(Patient).options(lazyload(Patient.history)).get(id_patient)
        p: Patient = self.session.query(Patient).options(joinedload(Patient.doctor)).options(joinedload(Patient.history)).get(id_patient)
        # p.doctor
        # print(p.history)
        self.session.close()
        return p


    def add(self, data: Patient):
        self.session.connection()
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        self.session.close()
        return self.session.query(Patient).get(data.id_patient)

    def addHealingHistoryPatient(self, healing_history: HealingHistory):
        self.session.connection()
        patient: Patient = self.session.query(Patient).get(healing_history.patient_id)
        patient.history.append(healing_history)
        self.session.commit()
        self.session.refresh(patient)
        self.session.close()
        return f'Добавлена новая история для: {patient.id_patient}'

    # def addHistoryNeuralNetwork(self):


    def find_all(self):
        self.session.connection()
        all = self.session.query(Patient).all().copy()
        self.session.close()
        return all

    def find_all_patient_fullname_and_snils(self):
        return self.session.query(Patient.id_patient,
                                  Patient.firstname,
                                  Patient.surname,
                                  Patient.middlename,
                                  Patient.snils).all()

    def delete_by_id(self, id_patient):
        self.session.connection()
        print('ИД: ========== ' + str(id_patient))
        patient = self.session.query(Patient).filter(Patient.id_patient == id_patient).first()
        self.session.delete(patient)
        self.session.commit()
        self.session.close()
        return 'Удаление успешно'


if __name__ == '__main__':
    engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)
    get_session = sessionmaker(engine)
    p = PatientRepository(1)
    # p.addHealingHistoryPatient(patient_id=5, healing_history=HealingHistory(comment='test25'))
    # patient = p.get(5)
    patient: Patient = p.getFullPatient(5)
    print(patient.doctor)
    print(patient.history)
    # patient.firstname = 'ivan2'
    # patient.history.append(HealingHistory(comment='test'))
    # patient.history.append(HealingHistory(comment='test1'))
    # patient.history.append(HealingHistory(comment='tes2'))
    # p.add(patient)
    # p.delete_by_id(2)
    # h = HealingHistory(comment='hsjhsgadjhfasgd')
    # patient: Patient = p.get(3)
    # print(patient)
    # patient.history = []
    # patient.history += h
    # for i in range(5):
    #     p.editPatient(patient)
    # new = Patient()
    # new.firstname = 'Максим'
    # print(p.add(new))
    # print(p.get(10).id_patient)
