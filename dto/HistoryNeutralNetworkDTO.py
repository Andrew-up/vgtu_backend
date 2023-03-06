import json

from model.model import HistoryNeuralNetwork, Annotations
from dto.ResultPredictDTO import ResultPredictDTO
from dto.AnnotationsDTO import AnnotationsDTO


class HistoryNeutralNetworkDTO(object):

    def __init__(self, **entries):
        self.id_history_neural_network = None
        self.photo_original = None
        self.photo_predict = None
        self.photo_predict_edit_doctor = None
        self.annotations: list[AnnotationsDTO] = []
        self.__dict__.update(entries)



    def getHistoryNeutralNetwork(self):
        h = HistoryNeuralNetwork()
        if self.photo_original is not None:
            h.photo_original = self.photo_original.encode('utf-8')
        if self.photo_predict is not None:
            h.photo_predict = self.photo_predict.encode('utf-8')
        if self.photo_predict_edit_doctor is not None:
            h.photo_predict_edit_doctor = self.photo_predict_edit_doctor.encode('utf-8')
        if self.annotations:
            for i in self.annotations:
                h.annotations.append(AnnotationsDTO(**i).getAnnotation())
        return h

    def getDto(self):
        dto = HistoryNeutralNetworkDTO()
        dto.id_history_neural_network = self.id_history_neural_network
        if self.photo_original is not None:
            dto.photo_original = self.photo_original.decode('utf-8')
        if self.photo_predict is not None:
            dto.photo_predict = self.photo_predict.decode('utf-8')
        if self.photo_predict_edit_doctor is not None:
            dto.photo_predict_edit_doctor = self.photo_predict_edit_doctor.decode('utf-8')
        if self.annotations is not None:
            for i in self.annotations:
                item = AnnotationsDTO(**i.__dict__).getDto()
                dto.annotations.append(item.__dict__)
        return dto

