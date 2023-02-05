from sqlalchemy import Column, Integer, String, BLOB, ForeignKey
from sqlalchemy.orm import relationship
from definitions import DATABASE_DIR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO:
# 1. подумать как хранить таблицы в разных файлах

# Таблица пациента
class Patient_model_back(Base):
    __tablename__ = 'Patient'
    id_patient = Column(Integer, primary_key=True)
    firstname = Column(String(250))
    surname = Column(String(250))
    middlename = Column(String(250))
    gender = Column(String(50))
    date_of_birth = Column(String(250))
    address = Column(String(250))
    phone = Column(String(250))
    polis_oms = Column(String(250))
    snils = Column(String(250))
    document = Column(String(250))
    dianosis = Column(String(250))
    date_healing_start = Column(String(250))
    date_healing_end = Column(String(250))
    history = relationship("HealingHistory", back_populates="patient")
    doctor = relationship("Doctor", back_populates="patient", uselist=False)
    photo = Column(BLOB)


# Child Patient->history
# История лечения пациента

class HealingHistory(Base):
    __tablename__ = 'Healing_history'
    id_healing_history = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey(Patient_model_back.id_patient))
    patient = relationship(Patient_model_back, back_populates="history")
    doctor = relationship("Doctor", back_populates="healing_history", uselist=False)
    comment = Column(String(500))
    date = Column(String(500))
    photo = Column(BLOB)

# Профиль доктора
class Doctor(Base):
    __tablename__ = 'Doctor'
    id_doctor = Column(Integer, primary_key=True)
    firstname = Column(String(250))
    surname = Column(String(250))
    middlename = Column(String(250))
    photo = Column(BLOB)
    patient_id = Column(Integer, ForeignKey(Patient_model_back.id_patient))
    patient = relationship(Patient_model_back, back_populates="doctor")
    healing_history_id = Column(Integer, ForeignKey(HealingHistory.id_healing_history))
    healing_history = relationship(HealingHistory, back_populates="doctor")



if __name__ == '__main__':
    engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)
    Base.metadata.create_all(engine)
