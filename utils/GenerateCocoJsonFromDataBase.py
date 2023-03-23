import ast
import base64
import json
import os.path
from ast import literal_eval
from io import BytesIO
from pathlib import Path


import matplotlib.pyplot as plt
import numpy as np

from service.HealingHistoryService import HealingHistoryService
from service.ResultPredictService import ResultPredictService
from definitions import ROOT_DIR
from PIL import Image, ImageOps
from model.model import HistoryNeuralNetwork
from dto.ResultPredictDTO import ResultPredictDTO
import shutil
from utils.read_xml_file import ReadXmlProject
import random

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

    def save_image_from_base64(self, base64_image_string, image_path, ann=None):
        img = Image.open(BytesIO(base64.b64decode(literal_eval(base64_image_string.decode('utf-8')))))
        img, mask = self.randomflip(img, ann)
        print('=======================')

        # print(ann.annotations)
        self.width = img.width
        self.height = img.height
        img.save(f'{image_path}/{self.file_name}', format='png')

        return img, mask

    def randomflip(self, image, mask):
        rand = random.getrandbits(1)
        rand = True
        image = np.array(image)
        # new_segmentation = []
        # new_bbox_list = []
        # print(mask.annotations[0].segmentation)
        if rand:
            # image = np.flip(image)
            print(len(mask.annotations))
            for index, i in enumerate(mask.annotations):
                train_mask = np.zeros((image.shape[0], image.shape[1], 1), dtype=np.uint8)
                print(train_mask.shape)
                print(i.segmentation)
                # img = rasterio.features.rasterize([poly], out_shape=(60, 50))
                # new_mask = np.zeros(image.shape)
                # resize = np.maximum(new_mask, )
                # print(new_mask.shape)
                pass
                # new_arr = str(np.rot90(np.array(ast.literal_eval(i.segmentation))).astype(float).tolist())
                # new_bbox = str(np.flip(np.array(ast.literal_eval(i.bbox))).astype(str).tolist())
                # mask.annotations[index].segmentation = new_arr
                # mask.annotations[index].bbox = new_bbox
        # print(mask.annotations[0].segmentation)
        # mask.annotations = new_segmentation
        return Image.fromarray(image), mask


class CocoJsonFormatClass(object):

    def __init__(self):
        # self.img = None

        self.info = info
        self.images: list[ImageObj] = []
        self.annotations: list[Annotations] = []
        self.categories: list[Categories] = []

    def addImage(self, string_base64=None, image_path=None, ann=None):
        image = ImageObj()
        if self.images:
            image.id = self.images[-1].id + 1
        else:
            image.id = 1
        image.file_name = f'{image.id}.png'
        img, mask = image.save_image_from_base64(string_base64, image_path, ann)
        self.images.append(image)
        # ann.annotations = mask
        # print(ann==mask)
        return image, mask

    def addAnnotation(self, img: ImageObj, history_nn: HistoryNeuralNetwork):
        for i in history_nn.annotations:
            annotation = Annotations()
            annotation.bbox = literal_eval(i.bbox)
            annotation.segmentation = [literal_eval(i.segmentation)]
            annotation.iscrowd = 0
            annotation.image_id = img.id
            annotation.area = i.area
            annotation.category_id = i.category_id
            if self.annotations:
                annotation.id = self.annotations[-1].id + 1
            else:
                annotation.id = 0
            self.annotations.append(annotation)

    def addCategories(self, catss: ResultPredictDTO.__dict__):
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
        self.copy_datasetToModelTraining()

    def printFolders(self):
        print(self.dataset_folder_path)
        print(self.annotation_folder_path)
        print(self.image_folder_path)

    def printImageId(self):
        data = self.service.getImageForDataset()
        all_cat = ResultPredictService(1).getAll()

        for j in all_cat:
            self.coco_class.addCategories(catss=j)
        # bbbbb = True
        # if bbbbb:

        for i in data:
            for j in range(1):
                # print(i.annotations)
                # pass
                # print(i.annotations[0].segmentation)
                new_image, mask = self.coco_class.addImage(string_base64=i.photo_original, image_path=self.image_folder_path, ann=i)
                self.coco_class.addAnnotation(img=new_image, history_nn=mask)
                # print(mask.annotations[0].segmentation)
                # return 0
                # print(mask == i)
                # pass
            pass

    def generateJsonFile(self):
        with open(ROOT_DIR + '/dataset/annotations/data.json', 'w', encoding='utf-8') as f:
            json.dump(self.coco_class.getJsonFull().__dict__, f, ensure_ascii=False, indent=4)
        return self.coco_class.getJsonFull().__dict__

    def createFolder(self):
        if os.path.exists(os.path.join(ROOT_DIR, 'dataset')):
            shutil.rmtree(os.path.join(ROOT_DIR, 'dataset'))

        Path(ROOT_DIR + '/dataset').mkdir(parents=True, exist_ok=True)
        Path(ROOT_DIR + '/dataset/annotations').mkdir(parents=True, exist_ok=True)
        Path(ROOT_DIR + '/dataset/image').mkdir(parents=True, exist_ok=True)

        self.dataset_folder_path = Path(ROOT_DIR + '/dataset')
        self.annotation_folder_path = Path(ROOT_DIR + '/dataset/annotations')
        self.image_folder_path = Path(ROOT_DIR + '/dataset/image')

    def copy_datasetToModelTraining(self):
        dataset_folder = os.path.join(ROOT_DIR, 'dataset')
        if os.path.exists(dataset_folder):
            to = os.path.join(ReadXmlProject().path_train_model, 'dataset')
            if os.path.exists(to):
                shutil.rmtree(to)
            shutil.copytree(dataset_folder, to)


if __name__ == '__main__':
    p = GenerateJsonFileFromDB()
    # print(p.getAll())
    pass
