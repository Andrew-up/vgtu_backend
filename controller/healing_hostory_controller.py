from flask import request, Response, send_from_directory, jsonify
from controller import app, API_ROOT
from model.model import HealingHistory
from service.HealingHistoryService import HealingHistoryService
import json
from dto import healingHistoryDTO
from service.patientService import PatientService


@app.route(API_ROOT + 'patient/history/<id_patient>/')
def getAllHistoryByPatientId(id_patient):
    print('1')
    s = HealingHistoryService(1)
    res: list[HealingHistory] = s.getAllHistoryByIdPatient(id_patient=id_patient)
    json_string = []
    for i in res:
        h: healingHistoryDTO.HealingHistoryDTO = healingHistoryDTO.HealingHistoryDTO(**i.__dict__).getDto()
        json_string.append(h.__dict__)
    return Response(json.dumps(json_string, ensure_ascii=False), status=200, headers={'Content-Type': 'application/json'})

@app.route(API_ROOT+'history/add/<id_patient>/',  methods=['POST'])
def add_history_patient(id_patient):
    print(id_patient)
    data: HealingHistory.__dict__ = request.json
    history = healingHistoryDTO.HealingHistoryDTO(**data).getHealingHistory()
    service = PatientService(1)
    # print(history)
    service.addHealingHistoryPatient(history)
    # print(data)
    # res = service.addHealingHistoryPatient(data)
    # print(res)
    return Response('1', status=200)

@app.route(API_ROOT + 'history/<id_history>/')
def get_history_by_history_id(id_history):
    s = HealingHistoryService(1)
    res: HealingHistory = s.getHistoryById(id_history)
    h: healingHistoryDTO.HealingHistoryDTO = healingHistoryDTO.HealingHistoryDTO(**res.__dict__).getDto().__dict__
    return Response(json.dumps(h), status=200,
                    headers={'Content-Type': 'application/json'})





