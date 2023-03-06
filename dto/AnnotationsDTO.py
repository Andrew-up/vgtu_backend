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
        self.__dict__.update(entries)



    def getAnnotation(self):
        a = Annotations()
        # a.id_annotations = self.id_annotations
        a.area = self.area
        a.bbox = self.bbox
        a.segmentation = self.segmentation
        # a.history_nn_id = self.history_nn_id
        if self.category_id is not None:
            a.category_id = self.category_id
        return a

    def getDto(self):
        dto = AnnotationsDTO()
        dto.id_annotations = self.id_annotations
        dto.bbox = self.bbox
        dto.segmentation = self.segmentation
        dto.history_nn_id = self.history_nn_id
        dto.category_id = self.category_id
        if self.result_predict is not None:
            dto.result_predict = ResultPredictDTO(**self.result_predict.__dict__).getDto().__dict__
        return dto

