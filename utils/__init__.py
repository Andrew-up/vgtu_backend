import sys
import os

# добавляем путь к текущей директории в sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# импортируем модули из зависимостей
from model.model import HealingHistory, ResultPredict, HistoryNeuralNetwork, Annotations, Patient
from repository.PatientRepository import PatientRepository
from repository.ResultPredictRepository import ResultPredictRepository
import datetime
