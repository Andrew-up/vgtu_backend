from sqlalchemy import Column, Integer, String, BLOB, ForeignKey, Float
from sqlalchemy.orm import relationship
from definitions import DATABASE_DIR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO:
# 1. подумать как хранить таблицы в разных файлах

# Таблица пациента
class Patient(Base):
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
    history: list["HealingHistory"] = relationship("HealingHistory", back_populates="patient", cascade="all,delete")
    doctor: "Doctor" = relationship("Doctor", back_populates="patient", uselist=False)
    photo = Column(BLOB)


#Результат распознавания нейронной сети
class ResultPredict(Base):
    __tablename__ = 'Result_predict'
    id_category = Column(Integer, primary_key=True)
    name_category_eng = Column(String(50))
    name_category_ru = Column(String(50))
    history_neural_network = relationship("HistoryNeuralNetwork", back_populates="result_predict", uselist=False)
    color = Column(String(50))

#История распознавания нейронной сети

class HistoryNeuralNetwork(Base):
    __tablename__ = 'History_neural_network'
    id_history_neural_network = Column(Integer, primary_key=True)
    photo_original = Column(BLOB)
    photo_predict = Column(BLOB)
    photo_predict_edit_doctor = Column(BLOB)
    polygon_mask = Column(BLOB)
    result_predict_id = Column(Integer, ForeignKey(ResultPredict.id_category))
    result_predict = relationship(ResultPredict, back_populates="history_neural_network", uselist=False)
    # healing_history_id = Column(Integer, ForeignKey("HealingHistory"."id_healing_history"))
    healing_history = relationship("HealingHistory", back_populates="history_neutral_network", uselist=False)
    area_wound = Column(Integer)
    annotations: list["Annotations"] = relationship("Annotations", back_populates="history_nn")

#История лечения пациента
class HealingHistory(Base):
    __tablename__ = 'Healing_history'
    id_healing_history = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey(Patient.id_patient))
    history_neural_network_id = Column(Integer, ForeignKey(HistoryNeuralNetwork.id_history_neural_network))
    history_neutral_network = relationship(HistoryNeuralNetwork, back_populates="healing_history")
    patient = relationship(Patient, back_populates="history")
    doctor = relationship("Doctor", back_populates="healing_history", uselist=False)
    comment = Column(String(500))
    date = Column(String(100))


class Annotations(Base):
    __tablename__ = 'Annotations_image'
    id_annotations = Column(Integer, primary_key=True)
    area = Column(Float(500))
    bbox = Column(String(500))
    segmentation = Column(String(500))
    history_nn_id = Column(Integer, ForeignKey(HistoryNeuralNetwork.id_history_neural_network))
    history_nn = relationship("HistoryNeuralNetwork", back_populates="annotations", uselist=False)
    category_id = Column(Integer)


# Профиль доктора
class Doctor(Base):
    __tablename__ = 'Doctor'
    id_doctor = Column(Integer, primary_key=True)
    firstname = Column(String(250))
    surname = Column(String(250))
    middlename = Column(String(250))
    photo = Column(BLOB)
    patient_id = Column(Integer, ForeignKey(Patient.id_patient))
    patient = relationship(Patient, back_populates="doctor")
    healing_history_id = Column(Integer, ForeignKey(HealingHistory.id_healing_history))
    healing_history = relationship(HealingHistory, back_populates="doctor")



if __name__ == '__main__':
    engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)
    Base.metadata.create_all(engine)
