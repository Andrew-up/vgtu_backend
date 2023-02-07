import json
import time

from flask import request, Response
from controller import app
from dto.patientDTO import PatientDTO, getPatient
from model.model import Patient_model_back
from service.patientService import PatientService

API_ROOT = '/api/'
SECRET_KEY = 'hFGHFEFyr67ggghhPJhdfh123dd'


@app.route(API_ROOT + "/all/")
def get_patients():
    p = PatientService(1)
    zzz = p.getAll()
    json_string = json.dumps([ob.__dict__ for ob in zzz], ensure_ascii=False)
    return json_string


@app.route(API_ROOT + 'patient/<id>/')
def get_patient_by_id(id):
    s_service = PatientService(1)
    p = s_service.getById(id)
    json_string = json.dumps(p.__dict__, ensure_ascii=False)
    return Response(json_string, status=200)


@app.route(API_ROOT + "/add/", methods=['POST'])
def add_new_patient():
    data1: PatientDTO.__dict__ = request.json
    dto = PatientDTO(**data1)
    s_service = PatientService(1)
    res = s_service.add(dto)
    print(res.address)
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
