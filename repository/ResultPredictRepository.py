from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from definitions import DATABASE_DIR
from model.model import ResultPredict, Annotations
from repository.abstractRepository import AbstractRepository

engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


class ResultPredictRepository(AbstractRepository):

    def __init__(self, doctor_id):
        self.session = sessionmaker(bind=engine)()
        self.doctor = doctor_id

    def get(self, id_category):
        pass

    def add(self, data: ResultPredict):
        self.session.connection()
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        self.session.close()
        return 'ok'


    def find_all(self) -> list[ResultPredict]:
        self.session.connection()
        all = self.session.query(ResultPredict).order_by(ResultPredict.id_category).all()
        self.session.close()
        return all
    def find_all_not_null(self) -> list[ResultPredict]:
        self.session.connection()
        all = self.session.query(ResultPredict).order_by(ResultPredict.id_category).join(Annotations).filter(ResultPredict.id_category==Annotations.category_id).all()
        self.session.close()
        return all


if __name__ == '__main__':
    p = ResultPredictRepository(1)
    sss = p.find_all_not_null()
    for i in sss:
        print(i.name_category_ru)
