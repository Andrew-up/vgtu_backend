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



def generate_new_version(version: str = None):
    n_version = list(version)
    if int(n_version[-1]) <= 99:
        n_version[-1] = str(int(n_version[-1])+1)
    if int(n_version[-1]) > 99:
        n_version[-1] = '0'
        n_version[2] = str(int(n_version[2])+1)
    if int(n_version[2]) > 99:
        n_version[2] = '0'
        n_version[0] = str(int(n_version[0])+1)
    print(''.join(n_version))
    return ''.join(n_version)


if __name__ == "__main__":
    generate_new_version()
    # m = MyClass()
    # m.start()
