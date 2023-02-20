from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from definitions import DATABASE_DIR
from model.model import ResultPredict
from repository.abstractRepository import AbstractRepository

engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


class ResultPredictRepository(AbstractRepository):

    def __init__(self, doctor_id):
        self.session = sessionmaker(bind=engine)()
        self.doctor = doctor_id

    def get(self, id_category):
        pass

    def add(self, data: ResultPredict):
        pass

    def find_all(self) -> list[ResultPredict]:
        self.session.connection()
        all = self.session.query(ResultPredict).all()
        self.session.close()
        return all


if __name__ == '__main__':
    p = ResultPredictRepository(1)
    sss = p.find_all()
    for i in sss:
        print(i.name_category_ru)
