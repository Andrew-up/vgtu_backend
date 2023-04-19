import sys
sys.path.append('../')
print(sys.path)

from model.model import HealingHistory, ResultPredict, HistoryNeuralNetwork, Annotations, Patient
from repository.PatientRepository import PatientRepository
from repository.ResultPredictRepository import ResultPredictRepository
import datetime


d = [{"id": 1, "cat_eng": 'cat1_1', "cat_ru": 'Асептическое 1 стадия', "color": (0, 0, 255)},
     {"id": 2, "cat_eng": 'cat1_2', "cat_ru": 'Асептическое 2 стадия', "color": (0, 0, 255)},
     {"id": 3, "cat_eng": 'cat1_3', "cat_ru": 'Асептическое 3 стадия', "color": (0, 0, 255)},
     {"id": 4, "cat_eng": 'cat2_1', "cat_ru": 'Бактериальное 1 стадия', "color": (0, 255, 0)},
     {"id": 5, "cat_eng": 'cat2_2', "cat_ru": 'Бактериальное 2 стадия', "color": (0, 255, 0)},
     {"id": 6, "cat_eng": 'cat2_3', "cat_ru": 'Бактериальное 3 стадия', "color": (0, 255, 0)},
     {"id": 7, "cat_eng": 'cat3_1', "cat_ru": 'Гнойное 1 стадия', "color": (255, 0, 0)},
     {"id": 8, "cat_eng": 'cat3_2', "cat_ru": 'Гнойное 2 стадия', "color": (255, 0, 0)},
     {"id": 9, "cat_eng": 'cat3_2', "cat_ru": 'Гнойное 3 стадия', "color": (255, 0, 0)}]

def add_result_predict_table():
    repo = ResultPredictRepository(1)
    for i in d:
        r = ResultPredict()
        r.id_category = i['id']
        r.name_category_eng = i['cat_eng']
        r.name_category_ru = i['cat_ru']
        r.color = str(i['color'])
        repo.add(r)


def gen_patient()->Patient:
    p = Patient()
    p.firstname = 'ivan'
    p.middlename = 'ivanayjvich'
    p.surname = 'ivanov'
    p.gender = 'male'
    p.snils = '123-123-123'
    return p

def gen_history()->HealingHistory:
    h = HealingHistory()
    h.date = str(datetime.datetime.now())
    h.comment = 'test123'
    return h

def gen_history_nn()->HistoryNeuralNetwork:
    h_nn = HistoryNeuralNetwork()
    h_nn.photo_original = b'133'
    h_nn.photo_predict = b'dshfsdf'
    return h_nn

def gen_ann()->Annotations:
    a = Annotations()
    a.bbox = '213,123,123,33'
    a.area = 1233.0
    a.segmentation = '[1,2,3,4,5,6,11,22,44]'
    a.category_id = 1
    return a


def gen():
    p = gen_patient()
    h = HealingHistory()
    h_nn = gen_history_nn()
    repo = PatientRepository(1)
    a = gen_ann()
    h_nn.annotations.append(a)
    h.history_neutral_network = h_nn
    p.history.append(h)
    repo.add(p)


if __name__ == '__main__':
    add_result_predict_table()
    # gen()