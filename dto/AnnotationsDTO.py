from dto.ResultPredictDTO import ResultPredictDTO
from model.model import Annotations
class AnnotationsDTO(object):
    def __init__(self, **entries):
        self.id_annotations: int = int()
        self.area: float = float()
        self.bbox: str = str()
        self.segmentation: str = str()
        self.history_nn_id: int = int()
        self.category_id: int = int()
        self.result_predict = None
        self.category = None
        self.__dict__.update(entries)



    def getAnnotation(self):
        a = Annotations()
        a.area = float(self.area)
        a.bbox = str(self.bbox)
        a.segmentation = str(self.segmentation)
        if self.category_id is not None:
            a.category_id = self.category_id
        print('111111111111111111')
        return a

    def getDto(self):
        dto = AnnotationsDTO()
        dto.id_annotations = self.id_annotations
        dto.bbox = self.bbox
        dto.segmentation = self.segmentation
        dto.history_nn_id = self.history_nn_id
        dto.category_id = self.category_id
        dto.area = self.area
        if self.result_predict is not None:
            dto.category = ResultPredictDTO(**self.result_predict.__dict__).getDto().__dict__
        return dto

