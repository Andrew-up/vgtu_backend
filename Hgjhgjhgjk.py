import subprocess
import threading
from model.model import ModelUnet
from repository.ModelUnetRepository import ModelUnetRepository
from time import sleep

class MyClass(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)
        self.history_cnn: MyClass() = None


    def run(self):
        print('1')
        self.add_history()
        path_python = 'D:/MyProgramm/vgtu_common/train_model/venv/Scripts/python.exe'
        s = subprocess.run(['python3', 'D:/MyProgramm/vgtu_common/train_model/main.py'],
                           executable=path_python, shell=False)
        # self.end_train_model()

    # def end_train_model(self):
    #     r = ModelUnetRepository(1)
    #     jjj = r.update(self.history_cnn)
    #     print(jjj)

    def add_history(self):
        model_1 = ModelUnet()
        r = ModelUnetRepository(1)
        model_1.status = 'train'
        self.history_cnn = r.add(model_1)






