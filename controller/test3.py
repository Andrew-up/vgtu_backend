import json
import time

from flask import request, Response
from controller import app
from dto.patientDTO import PatientDTO, getPatient
from model.model import Patient_model_back
from service.patientService import PatientService

API_ROOT = '/api/'


@app.route(API_ROOT + "/all/")
def hello_world22():
    start = time.time()
    p = PatientService(1)
    zzz = p.getAll()
    json_string = json.dumps([ob.__dict__ for ob in zzz], ensure_ascii=False)
    roundtrip = time.time() - start
    print(f'roundtrip: {roundtrip}')
    return json_string


@app.route(API_ROOT + 'patient/<id>/')
def get_patient_by_id(id):
    print(id)
    s_service = PatientService(1)
    p = s_service.getById(id)
    json_string = json.dumps(p.__dict__, ensure_ascii=False)
    return Response(json_string, status=200)


@app.route(API_ROOT + "/add/", methods=['POST'])
def add_new_patient():
    data1: PatientDTO.__dict__ = request.json
    s = PatientDTO(**data1)
    patient: Patient_model_back = getPatient(s)

    # getPatient(data)

    # x = json.loads(data)
    # print(x)
    # print(x.id_patient)
    # p = PatientService(1)
    # zzz = p.add()
    # json_string = json.dumps([ob.__dict__ for ob in zzz], ensure_ascii=False)
    return Response('OK', 200)
