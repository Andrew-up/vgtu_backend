from definitions import ROOT_DIR
import os.path
import xml.etree.ElementTree as ET


class ReadXmlProject(object):

    def __init__(self):
        self.file_path = os.path.join(ROOT_DIR, 'project.xml')
        self._path_train_model = None
        self._path_python_interceptor = None
        self._path_ann_file = None
        self._path_dataset_image = None
        self._name_script = None
        self._model_path = None
        self._model_name = None
        self._init_variable()


    def _init_variable(self):
        if os.path.exists(self.file_path):
            root_node = ET.parse(self.file_path).getroot()
            train_model = root_node.find('train_model')
            self._path_train_model = train_model.find('path_train_model').text
            self._path_python_interceptor = train_model.find('path_python_interceptor').text
            self._path_ann_file = train_model.find('path_ann_file').text
            self._path_dataset_image = train_model.find('path_dataset_image').text
            self._name_script = train_model.find('name_script').text
            self._model_path = train_model.find('model_path').text
            # self._model_name = train_model.find('model_name').text
        else:
            print(f'не найден {self.file_path}')

    @property
    def path_train_model(self):
        return self._path_train_model

    @property
    def path_python_interceptor(self):
        return self._path_python_interceptor

    @property
    def path_ann_file(self):
        return self._path_ann_file

    @property
    def path_dataset_image(self):
        return self._path_dataset_image

    @property
    def name_script(self):
        return self._name_script

    @property
    def model_path(self):
        return self._model_path

    @property
    def model_name(self):
        return self._model_name





if __name__ == '__main__':
    r = ReadXmlProject()
    print(r.path_python_interceptor)
