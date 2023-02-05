from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from model.model import Patient_model_back
from repository.abstractRepository import AbstractRepository
from definitions import DATABASE_DIR
engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


class PatientRepository(AbstractRepository):

    def __init__(self, doctor_id):
        self.session = sessionmaker(bind=engine)()
        self.doctor = doctor_id

    def get(self, id_patient) -> Patient_model_back:
        self.session.connection()
        get = self.session.query(Patient_model_back).get(id_patient)
        self.session.close()
        return get

    def add(self, data: Patient_model_back):
        self.session.connection()
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        self.session.close()
        return self.session.query(Patient_model_back).get(data.id_patient)

    def find_all(self):
        self.session.connection()
        all = self.session.query(Patient_model_back).all()
        self.session.close()
        return all

    def find_all_patient_fullname_and_snils(self):
        return self.session.query(Patient_model_back.id_patient,
                                  Patient_model_back.firstname,
                                  Patient_model_back.surname,
                                  Patient_model_back.middlename,
                                  Patient_model_back.snils).all()

    def delete_by_id(self, id_patient):
        self.session.connection()
        print('ИД: ========== ' + str(id_patient))
        self.session.query(Patient_model_back).filter(Patient_model_back.id_patient==id_patient).delete()
        self.session.commit()
        self.session.close()
        return 'Удаление успешно'


if __name__ == '__main__':
    engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)
    get_session = sessionmaker(engine)
    p = PatientRepository()
    new = Patient_model_back()
    new.firstname = 'Максим'
    # print(p.add(new))
    # print(p.get(10).id_patient)



