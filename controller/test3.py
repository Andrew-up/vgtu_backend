import json
import logging
import os

from flask import request, Response

from controller import app, API_ROOT
from definitions import RELEASE_DIR, VERSION
from dto.patientDTO import PatientDTO
from service.patientService import PatientService

# logger2 = logging.basicConfig(level=logging.WARNING)
logger2 = logging.getLogger('test1')
logger2.setLevel(level=logging.DEBUG)

file = logging.FileHandler('test1.log')
basic_format_left = logging.Formatter(
    '%(asctime)s : [%(levelname)s] : %(message)s IP-CLIENT: %(ip_client)-15s url: %(url)-100s')
file.setFormatter(basic_format_left)
logger2.addHandler(file)
# logger.set

for kei in logging.Logger.manager.loggerDict:
    print(kei)

SECRET_KEY = 'hFGHFEFyr67ggghhPJhdfh123dd'

testssss = {
    'ip_client': None,
    'url': None
}


@app.route(API_ROOT + "/all/")
def get_patients():
    p = PatientService(1)
    zzz = p.getAll()
    remote_addr = request
    testssss['ip_client'] = remote_addr.remote_addr
    testssss['url'] = remote_addr.path
    print(testssss)
    logger2.debug(f'test', extra=testssss)
    json_string = json.dumps([ob.__dict__ for ob in zzz], ensure_ascii=False)
    return json_string


@app.route(API_ROOT + 'patient/<id>/')
def get_patient_by_id(id):
    s_service = PatientService(1)
    p = s_service.getById(id)
    json_string = json.dumps(p.__dict__, ensure_ascii=False)
    return Response(json_string, status=200)


@app.route('/api/app/version/')
def check_version():
    # logger2.debug(f'test: {VERSION}')
    # print(request)
    remote_addr = request
    testssss['ip_client'] = remote_addr.remote_addr
    testssss['url'] = remote_addr.path
    # print(remote_addr)
    print(testssss)
    logger2.debug(f'test', extra=testssss)
    print(VERSION)
    return Response(VERSION, status=200)


@app.route('/api/app/update/download/')
def download():
    with open(os.path.join(RELEASE_DIR, 'test.zip'), 'rb') as f:
        data = f.readlines()
        return Response(data, headers={
            'Content-Type': 'application/zip',
            'Content-Disposition': 'attachment; filename=update.zip;'}
                        )


@app.route(API_ROOT + "/add/", methods=['POST'])
def add_new_patient():
    data1: PatientDTO.__dict__ = request.json
    dto = PatientDTO(**data1)
    s_service = PatientService(1)
    res = s_service.add(dto)
    json_string = json.dumps(res.__dict__, ensure_ascii=False)
    return Response(json_string, 200)


@app.route(API_ROOT + 'patient/delete/<id>', methods=['POST', 'GET'])
def delete_patient(id):
    if request.method == 'POST':
        r = request.json
        if r['key'] == SECRET_KEY:
            print('delete')
            srvise = PatientService(1)
            res = srvise.deletePatientById(id_patient=id)
            return Response(res, 200)
    else:
        return Response('Ошибка доступа', 401)
