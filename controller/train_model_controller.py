import json
import os

from flask import Response, request

from Hgjhgjhgjk import MyClass
from controller import app, API_ROOT
from dto.ModelUnetDTO import ModelUnetDTO, ModelUnet
from repository.ModelUnetRepository import ModelUnetRepository
from utils.GenerateCocoJsonFromDataBase import GenerateJsonFileFromDB


@app.route(API_ROOT + '/model_cnn/train/')
def train_model():
    dto = ModelUnetDTO()
    r = ModelUnetRepository(1)
    data = r.get_last_history_train()
    if data is None:
        m = ModelUnet()
        m.status = 'Начат процесс обучения'
        new_data = r.add(m)
        dto = ModelUnetDTO(**new_data.__dict__).getDTO()
        ooooo = MyClass()
        ooooo.start()
    else:
        if data.status == 'train':
            dto = ModelUnetDTO(**data.__dict__).getDTO()
            dto.status = 'Идет процесс обучения'
        if data.status != 'train':
            dto = ModelUnetDTO(**data.__dict__).getDTO()
            dto.status = 'Подождите'
        if data.status == 'compleated':
            m = ModelUnet()
            m.status = 'Начат процесс обучения'
            new_data = r.add(m)
            myclass = MyClass()
            myclass.start()
            dto = ModelUnetDTO(**new_data.__dict__).getDTO()

    return Response(json.dumps(dto.__dict__, ensure_ascii=False), status=200,
                    headers={'Content-Type': 'application/json'})


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


@app.route(API_ROOT + '/model_cnn/add/', methods=['POST'])
def add_history_model():
    data: ModelUnet = ModelUnetDTO(**request.json).getModelUnet()
    repo = ModelUnetRepository(1)
    repo.add(data)
    print(data.status)
    return Response('ok', 200)
