import json

from flask import Response

from controller import app, API_ROOT
from service.ResultPredictService import ResultPredictService


@app.route(API_ROOT + 'categorical/all/')
def getAllCategorical():
    print('1')
    s = ResultPredictService(1)
    res = s.getAll()
    return Response(json.dumps(res, ensure_ascii=False), status=200, headers={'Content-Type': 'application/json'})
@app.route(API_ROOT + 'categorical/all_not_null/')
def getAllCategoricalNotNull():
    s = ResultPredictService(1)
    res = s.getAllNotNull()
    return Response(json.dumps(res, ensure_ascii=False), status=200, headers={'Content-Type': 'application/json'})
