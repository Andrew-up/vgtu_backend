from flask import request, Response, send_from_directory, jsonify
from controller import app, API_ROOT
from model.model import HealingHistory
from service.ResultPredictService import ResultPredictService
import json
from dto import healingHistoryDTO
from service.patientService import PatientService


@app.route(API_ROOT + 'categorical/all/')
def getAllCategorical():
    print('1')
    s = ResultPredictService(1)
    res = s.getAll()
    return Response(json.dumps(res, ensure_ascii=False), status=200, headers={'Content-Type': 'application/json'})

