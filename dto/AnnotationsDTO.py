from model.model import Annotations
class AnnotationsDTO(object):
    def __init__(self, **entries):
        self.id_annotations = None
        self.area = None
        self.bbox = None
        self.segmentation = None
        self.history_nn_id = None
        self.category_id = None
        self.__dict__.update(entries)
        print('=========================')
        print(self.id_annotations)


    def getAnnotation(self):
        a = Annotations()
        a.id_annotations = self.id_annotations
        a.area = self.area
        a.bbox = self.bbox
        a.segmentation = self.segmentation
        a.history_nn_id = self.history_nn_id
        a.category_id = self.category_id
        return a

    def getDto(self):
        dto = AnnotationsDTO()
        dto.id_annotations = self.id_annotations
        dto.bbox = self.bbox
        dto.segmentation = self.segmentation
        dto.history_nn_id = self.history_nn_id
        dto.category_id = self.category_id
        return dto

