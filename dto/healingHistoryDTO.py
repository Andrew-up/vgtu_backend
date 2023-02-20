import json

from  model.model  import HealingHistory, HistoryNeuralNetwork, ResultPredict
from dto.HistoryNeutralNetworkDTO import HistoryNeutralNetworkDTO


class HealingHistoryDTO(object):

    def __init__(self, **entries):
        self.id_healing_history = None
        self.patient_id = None
        self.comment = None
        self.date = None
        self.history_neural_network_id = None
        self.doctor = None
        self.history_neutral_network = None
        self.__dict__.update(entries)

    def getHealingHistory(self):
        h = HealingHistory()
        h.id_healing_history = self.id_healing_history
        h.patient_id = self.patient_id
        h.comment = self.comment
        h.doctor = self.doctor
        h.history_neural_network_id = self.history_neural_network_id
        if self.history_neutral_network is not None:
            h.history_neutral_network = HistoryNeutralNetworkDTO(**self.history_neutral_network).getHistoryNeutralNetwork()
        return h

    def getDto(self):
        dto = HealingHistoryDTO()
        dto.id_healing_history = self.id_healing_history
        dto.patient_id = self.patient_id
        dto.comment = self.comment
        dto.date = self.date
        dto.history_neural_network_id = self.history_neural_network_id
        if self.history_neutral_network is not None:
            dto.history_neutral_network = HistoryNeutralNetworkDTO(**self.history_neutral_network.__dict__).getDto().__dict__
        return dto

