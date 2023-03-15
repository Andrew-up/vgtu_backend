import os.path
import subprocess
import threading
from model.model import ModelUnet
from repository.ModelUnetRepository import ModelUnetRepository
from time import sleep

from utils.read_xml_file import ReadXmlProject


class MyClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.xml = ReadXmlProject()

    def run(self):
        print('ssssssssssssss')
        path_script = os.path.join(self.xml.path_train_model, self.xml.name_script)
        subprocess.run(['python3', path_script],
                       executable=self.xml.path_python_interceptor, shell=False)


# if __name__ == "__main__":
#     m = MyClass()
#     m.start()
