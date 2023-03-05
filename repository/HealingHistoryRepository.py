from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload, subqueryload
from sqlalchemy import func

from definitions import DATABASE_DIR
from model.model import HealingHistory, ResultPredict, HistoryNeuralNetwork
from repository.abstractRepository import AbstractRepository

engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


class HealingHistoryRepository(AbstractRepository):

    def __init__(self, doctor_id):
        self.session = sessionmaker(bind=engine)()
        self.doctor = doctor_id

    def get(self, id_history) -> HealingHistory:
        self.session.connection()
        history: HealingHistory = self.session.query(HealingHistory).filter(
            HealingHistory.id_healing_history == id_history) \
            .join(HistoryNeuralNetwork, isouter=True) \
            .join(ResultPredict, isouter=True) \
            .options(
            joinedload(HealingHistory.history_neutral_network).subqueryload(HistoryNeuralNetwork.result_predict)).first()
        # get: HealingHistory = self.session.query(HealingHistory).get(id_history)
        self.session.close()
        return history

    def add(self, data: HealingHistory):
        self.session.connection()
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        self.session.close()
        return self.session.query(HealingHistory).get(data.id_healing_history)


    def getAllHistoryByPatientId(self, id_patient) -> list[HealingHistory]:
        self.session.connection()
        all_history_patient: list[HealingHistory] = self.session.query(HealingHistory).filter(HealingHistory.patient_id == id_patient)\
            .join(HistoryNeuralNetwork, isouter=True)\
            .join(ResultPredict, isouter=True)\
            .options(joinedload(HealingHistory.history_neutral_network).subqueryload(HistoryNeuralNetwork.result_predict)).all()
        self.session.close()
        return all_history_patient


    def getImageDataset(self):
        self.session.connection()
        dataset = self.session.query(HistoryNeuralNetwork).filter(HistoryNeuralNetwork.photo_predict_edit_doctor != None)\
            .join(ResultPredict, isouter=True).options(joinedload(HistoryNeuralNetwork.result_predict)).all()
        self.session.close()
        return dataset


if __name__ == '__main__':
    r = HealingHistoryRepository(1)
    for i in r.getImageDataset():
        # print(i.id_history_neural_network)
        print(i.result_predict)
    # print(r.hfhjgsdfjsdgf())
    # r.getAllHistoryByPatientId(5)
    # for i in r.getAllHistoryByPatientId(5):
    #     print(i.history_neutral_network.result_predict.name_category_ru)

    # print(len(r.getAllHistoryByPatientId(5)))
    # print(r.get(1).comment)
