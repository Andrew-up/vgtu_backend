import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.model import HealingHistory, ResultPredict, HistoryNeuralNetwork, Annotations, Patient
from repository.PatientRepository import PatientRepository
from repository.ResultPredictRepository import ResultPredictRepository
import datetime