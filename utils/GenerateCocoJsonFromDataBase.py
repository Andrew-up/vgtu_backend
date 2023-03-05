import base64
import json
import os.path
from ast import literal_eval
from io import BytesIO
from pathlib import Path
from service.HealingHistoryService import HealingHistoryService
from service.ResultPredictService import ResultPredictService
from definitions import ROOT_DIR
from PIL import Image
from model.model import HistoryNeuralNetwork
from dto.ResultPredictDTO import ResultPredictDTO


info = {
    "description": "my-project-name"
}


class Categories(object):
    def __init__(self):
        self.id = 0
        self.name = ''


class Annotations(object):
    def __init__(self):
        self.id: int = 0
        self.iscrowd: int = 0
        self.image_id: int = 0
        self.category_id: int = 0
        self.segmentation = []
        self.bbox = []
        self.area = 0


class ImageObj(object):

    def __init__(self):
        self.id: int = 0
        self.width: int = 512
        self.height: int = 512
        self.file_name: str = ''

    def save_image_from_base64(self, base64_image_string, image_path):
        img = Image.open(BytesIO(base64.b64decode(literal_eval(base64_image_string.decode('utf-8')))))
        self.width = img.width
        self.height = img.height
        img.save(f'{image_path}/{self.file_name}', format='png')


class CocoJsonFormatClass(object):

    def __init__(self):
        self.info = info
        self.images: list[ImageObj] = []
        self.annotations: list[Annotations] = []
        self.categories: list[Categories] = []

    def addImage(self, string_base64=None, image_path=None):
        image = ImageObj()
        if self.images:
            image.id = self.images[-1].id + 1
        else:
            image.id = 1
        image.file_name = f'{image.id}.png'
        image.save_image_from_base64(string_base64, image_path)
        self.images.append(image)
        # print(image.__dict__)
        return image

    def addAnnotation(self, img: ImageObj, history_nn: HistoryNeuralNetwork):
        annotation = Annotations()
        if self.annotations:
            annotation.id = self.annotations[-1].id + 1
        else:
            annotation.id = 1
        # annotation.segmentation.append(ann.segmentation)
        annotation.iscrowd = 0
        annotation.image_id = img.id
        annotation.category_id = history_nn.result_predict_id
        str = history_nn.polygon_mask.decode('utf-8')
        res = base64.b64decode(literal_eval(str)).decode('utf-8')
        annotation.segmentation = literal_eval(res)
        annotation.area = history_nn.area_wound

        b = b'WwogICAgICAgICAgICAxMjgsCiAgICAgICAgICAgIDczLjU3NDgwMzE0OTYwNjMsCiAgICAgICAgICAgIDE4My40MzMwNzA4NjYxNDE3NSwKICAgICAgICAgICAgMjAwLjU2NjkyOTEzMzg1ODI1CiAgICAgICAgIF0='
        ff = base64.b64decode(b).decode('utf-8')
        # print(ff)
        # s = [2,3,5,7]
        annotation.bbox.append(literal_eval(ff))
        # print(type(s))
        self.annotations.append(annotation)

    def addCategories(self, catss: ResultPredictDTO):
        cat = Categories()
        cat.id = catss['id_category']
        cat.name = catss['name_category_eng']
        self.categories.append(cat)


    def getJsonImages(self):
        return json.dumps(self.images, default=lambda x: x.__dict__)

    def getJsonAnnotations(self):
        return json.dumps(self.annotations, default=lambda x: x.__dict__)

    def getJsonCategories(self):
        return json.dumps(self.categories, default=lambda x: x.__dict__)

    def getJsonFull(self):
        c = CocoJsonFormatClass()
        c.images = json.loads(self.getJsonImages())
        c.annotations = json.loads(self.getJsonAnnotations())
        c.categories = json.loads(self.getJsonCategories())
        return c


class GenerateJsonFileFromDB(object):

    def __init__(self):
        self.service = HealingHistoryService(1)
        self.coco_class = CocoJsonFormatClass()
        self.dataset_folder_path = None
        self.annotation_folder_path = None
        self.image_folder_path = None
        self.createFolder()

        self.printImageId()
        self.generateJsonFile()

    def printFolders(self):
        print(self.dataset_folder_path)
        print(self.annotation_folder_path)
        print(self.image_folder_path)

    def printImageId(self):
        data = self.service.getImageForDataset()
        all_cat = ResultPredictService(1).getAll()

        for j in all_cat:
            self.coco_class.addCategories(catss=j)

        for i in data:
            new_image = self.coco_class.addImage(string_base64=i.photo_original,  image_path=self.image_folder_path)
            self.coco_class.addAnnotation(img=new_image, history_nn=i)



    def generateJsonFile(self):
        with open(ROOT_DIR + '/dataset/annotations/data.json', 'w', encoding='utf-8') as f:
            json.dump(self.coco_class.getJsonFull().__dict__, f,  ensure_ascii=False, indent=4)


    def createFolder(self):
        Path(ROOT_DIR + '/dataset').mkdir(parents=True, exist_ok=True)
        Path(ROOT_DIR + '/dataset/annotations').mkdir(parents=True, exist_ok=True)
        Path(ROOT_DIR + '/dataset/image').mkdir(parents=True, exist_ok=True)

        self.dataset_folder_path = Path(ROOT_DIR + '/dataset')
        self.annotation_folder_path = Path(ROOT_DIR + '/dataset/annotations')
        self.image_folder_path = Path(ROOT_DIR + '/dataset/image')




#

if __name__ == '__main__':
    p = GenerateJsonFileFromDB()
    # print(p.getAll())
    pass
