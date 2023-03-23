from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload, subqueryload
from sqlalchemy import func

from definitions import DATABASE_DIR
from model.model import HealingHistory, ResultPredict, HistoryNeuralNetwork, Annotations
from repository.abstractRepository import AbstractRepository

engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


class HealingHistoryRepository(AbstractRepository):

    def __init__(self, doctor_id):
        self.session = sessionmaker(bind=engine)()
        self.doctor = doctor_id

    def get(self, id_history) -> HealingHistory:
        self.session.connection()
        history: HealingHistory = self.session.query(HealingHistory) \
            .join(HistoryNeuralNetwork, isouter=True) \
            .join(Annotations, isouter=True)\
            .join(ResultPredict, isouter=True)\
            .filter(HealingHistory.id_healing_history == id_history)\
            .filter(Annotations.history_nn_id == HistoryNeuralNetwork.id_history_neural_network)\
            .filter(ResultPredict.id_category == Annotations.category_id)\
            .options(
            joinedload(HealingHistory.history_neutral_network)
            .subqueryload(HistoryNeuralNetwork.annotations)
            .joinedload(Annotations.result_predict)).first()
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
        all_history_patient: list[HealingHistory] = self.session.query(HealingHistory)\
            .join(HistoryNeuralNetwork, isouter=True) \
            .join(Annotations, isouter=True)\
            .join(ResultPredict, isouter=True)\
            .filter(HealingHistory.patient_id == id_patient)\
            .filter(Annotations.history_nn_id == HistoryNeuralNetwork.id_history_neural_network) \
            .options(
            joinedload(HealingHistory.history_neutral_network)
            .subqueryload(HistoryNeuralNetwork.annotations)
            .joinedload(Annotations.result_predict)).all()
        self.session.close()
        # print(all_history_patient[-1].history_neutral_network.annotations[-1].bbox)
        return all_history_patient


    def getImageDataset(self):
        self.session.connection()
        dataset = self.session.query(HistoryNeuralNetwork).filter(HistoryNeuralNetwork.photo_predict_edit_doctor != None)\
            .join(Annotations, isouter=True).options(joinedload(HistoryNeuralNetwork.annotations))\
            .order_by(HistoryNeuralNetwork.id_history_neural_network.desc()).all()
        self.session.close()
        return dataset


if __name__ == '__main__':
    r = HealingHistoryRepository(1)
    res = r.getImageDataset()
    # print(res)
    # ann = res.history_neutral_network.annotations
    # for i in ann:
    #     print(i.bbox)

    # for i in r.getImageDataset():
        # print(i.id_history_neural_network)
        # print(i.result_predict)
    # print(r.hfhjgsdfjsdgf())
    # r.getAllHistoryByPatientId(5)
    # for i in r.getAllHistoryByPatientId(5):
    #     print(i.history_neutral_network.result_predict.name_category_ru)

    # print(len(r.getAllHistoryByPatientId(5)))
    # print(r.get(1).comment)
