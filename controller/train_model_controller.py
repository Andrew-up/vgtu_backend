import json
from flask import Response, request

from Hgjhgjhgjk import MyClass
from controller import app, API_ROOT
from repository.ModelUnetRepository import ModelUnetRepository
from service.ResultPredictService import ResultPredictService
from utils.GenerateCocoJsonFromDataBase import GenerateJsonFileFromDB
from dto.ModelUnetDTO import ModelUnetDTO, ModelUnet


@app.route(API_ROOT + '/model_cnn/train/')
def train_model():
    repo = ModelUnetRepository(1)
    model_history = repo.get_last_history_train()
    dto = ModelUnetDTO()
    if model_history:
        if model_history.status == 'train':
            dto = ModelUnetDTO(**model_history.__dict__).getDTO()
        else:
            myclass = MyClass()
            myclass.start()
            dto.status = 'Начато обучение модели, подождите для получения статистики'
    else:
        myclass = MyClass()
        myclass.start()
        dto.status = 'Начато обучение модели, подождите для получения статистики'

    return Response(json.dumps(dto.__dict__, ensure_ascii=False), status=200, headers={'Content-Type': 'application/json'})


@app.route(API_ROOT + "/ann_json/")
def get_ann_json():
    p = GenerateJsonFileFromDB()
    r = ModelUnetRepository(1)
    data = r.get_last_history_train()
    if data:
        if data.status == 'train':
            return 'модель уже обучается, подождите'
    myclass = MyClass()
    myclass.start()
    return p.generateJsonFile()


@app.route(API_ROOT + '/model_cnn/update/', methods=['POST'])
def update_model():
    data: ModelUnet = ModelUnetDTO(**request.json).getModelUnet()
    repo = ModelUnetRepository(1)
    repo.update(data)
    print(data.status)
    return Response('ok', 200)
