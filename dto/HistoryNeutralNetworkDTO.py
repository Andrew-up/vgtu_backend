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
        self.polygon_mask = None
        self.result_predict = None
        self.result_predict_id = None
        self.area_wound = None
        self.annotations: list[AnnotationsDTO] = []
        self.__dict__.update(entries)


    def getHistoryNeutralNetwork(self):
        h = HistoryNeuralNetwork()
        # h.id_history_neural_network = self.id_history_neural_network
        if self.photo_original is not None:
            h.photo_original = self.photo_original.encode('utf-8')
        if self.photo_predict is not None:
            h.photo_predict = self.photo_predict.encode('utf-8')
        if self.photo_predict_edit_doctor is not None:
            h.photo_predict_edit_doctor = self.photo_predict_edit_doctor.encode('utf-8')
        if self.polygon_mask is not None:
            h.polygon_mask = self.polygon_mask.encode('utf-8')
        if self.result_predict_id is not None:
            h.result_predict_id = self.result_predict_id
        if self.area_wound is not None and self.area_wound > 0:
            h.area_wound = self.area_wound
        return h

    def getDto(self):
        dto = HistoryNeutralNetworkDTO()
        dto.id_history_neural_network = self.id_history_neural_network
        if self.result_predict is not None:
            dto.result_predict = ResultPredictDTO(**self.result_predict.__dict__).getDto().__dict__
        if self.photo_original is not None:
            dto.photo_original = self.photo_original.decode('utf-8')
        if self.photo_predict is not None:
            dto.photo_predict = self.photo_predict.decode('utf-8')
        if self.photo_predict_edit_doctor is not None:
            dto.photo_predict_edit_doctor = self.photo_predict_edit_doctor.decode('utf-8')
        if self.polygon_mask is not None:
            dto.polygon_mask = self.polygon_mask.decode('utf-8')
        if self.area_wound is not None and self.area_wound > 0:
            dto.area_wound = self.area_wound
        print('================')
        print(self.annotations)
        if self.annotations is not None:
            for i in self.annotations:
                item = AnnotationsDTO(**i.__dict__).getDto()
                dto.annotations.append(item.__dict__)
        del dto.result_predict_id
        return dto

