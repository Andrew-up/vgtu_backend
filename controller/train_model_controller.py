import json
import os
import zipfile
from io import BytesIO

from flask import Response, request, send_file, stream_with_context

from Hgjhgjhgjk import MyClass
from controller import app, API_ROOT
from dto.ModelUnetDTO import ModelUnetDTO, ModelUnet
from repository.ModelUnetRepository import ModelUnetRepository
from utils.GenerateCocoJsonFromDataBase import GenerateJsonFileFromDB
from utils.read_xml_file import ReadXmlProject


@app.route(API_ROOT + '/model_cnn/last_model/')
def get_last_history():
    r = ModelUnetRepository(1)
    void_history = ModelUnetDTO()
    data = r.get_last_history_train()
    if data:
        data = ModelUnetDTO(**data.__dict__).getDTO()
        return Response(json.dumps(data.__dict__, ensure_ascii=False), status=200,
                        headers={'Content-Type': 'application/json'})
    return Response(json.dumps(void_history.__dict__, ensure_ascii=False), status=200,
                    headers={'Content-Type': 'application/json'})


CHUNK_SIZE = 8192
def read_file_chunks(path):
    with open(path, 'rb') as fd:
        while 1:
            buf = fd.read(CHUNK_SIZE)
            if buf:
                yield buf
            else:
                break

@app.route(API_ROOT + '/model_cnn/last_model/download/')
def get_last_history_download():
    r = ModelUnetRepository(1)
    data = r.get_last_history_train()
    r = ReadXmlProject()
    if data:
        full_path = os.path.join(r.path_train_model+r.model_path, data.name_file)
        zip_name = f'{os.path.splitext(full_path)[0]}.zip'
        return Response(
            stream_with_context(read_file_chunks(zip_name)),
            headers={
                'Content-Disposition': f'attachment; filename={os.path.splitext(data.name_file)[0]}.zip'
            })
    return 'ok'


def generate_new_version(version: str = None):
    version_str = '1.0.0'
    print(version)
    print('SSSSSSSSSSSSSSSSSSSSS')
    if version is not None:
        n_version = list(version)
        if int(n_version[-1]) <= 99:
            n_version[-1] = str(int(n_version[-1]) + 1)
        if int(n_version[-1]) > 99:
            n_version[-1] = '0'
            n_version[2] = str(int(n_version[2]) + 1)
        if int(n_version[2]) > 99:
            n_version[2] = '0'
            n_version[0] = str(int(n_version[0]) + 1)

        version_str = ''.join(n_version)
    return version_str


@app.route(API_ROOT + '/model_cnn/train/')
def train_model():
    dto = ModelUnetDTO()
    r = ModelUnetRepository(1)
    data = r.get_last_history_train()
    if data is None or data.status == 'compleated':
        m = ModelUnet()
        m.status = 'Начат процесс обучения'
        if data:
            m.version = data.version
        m.version = generate_new_version(m.version)
        m.name_file = f'model_{m.version.replace(".","_")}.h5'
        new_data = r.add(m)
        dto = ModelUnetDTO(**new_data.__dict__).getDTO()
        ooooo = MyClass()
        ooooo.start()
    else:
        if data.status == 'train':
            dto = ModelUnetDTO(**data.__dict__).getDTO()
            dto.status = 'Идет процесс обучения'
        else:
            dto = ModelUnetDTO(**data.__dict__).getDTO()
            dto.status = 'Подождите'

    return Response(json.dumps(dto.__dict__, ensure_ascii=False), status=200,
                    headers={'Content-Type': 'application/json'})


@app.route(API_ROOT + "/ann_json/")
def get_ann_json():
    p = GenerateJsonFileFromDB()
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
