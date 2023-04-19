import sys
import os
print(sys.path)

from model.model import HealingHistory, ResultPredict, HistoryNeuralNetwork, Annotations, Patient
from repository.PatientRepository import PatientRepository
from repository.ResultPredictRepository import ResultPredictRepository
import datetime