from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from definitions import DATABASE_DIR
from model.model import ModelUnet
from repository.abstractRepository import AbstractRepository

engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


class ModelUnetRepository(AbstractRepository):

    def __init__(self, doctor_id):
        self.session = sessionmaker(bind=engine)()
        self.doctor = doctor_id

    def get(self, id_category):
        pass

    def add(self, data: ModelUnet):
        self.session.connection()
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        self.session.close()
        return data

    def update(self, new_history: ModelUnet):
        self.session.connection()
        #Получение истории обучения по id
        history: ModelUnet = self.session.query(ModelUnet).get(new_history.id)

        # Обновление данных

        history.status = new_history.status
        # ------------

        self.session.add(history)
        self.session.commit()
        self.session.refresh(history)
        self.session.close()
        return history


    def get_last_history_train(self) -> ModelUnet:
        self.session.connection()
        m = self.session.query(ModelUnet).order_by(ModelUnet.id.desc()).first()
        self.session.close()
        return m



if __name__ == '__main__':
    p = ModelUnetRepository(1)
    sss = p.get_last_history_train()
    print(sss)
