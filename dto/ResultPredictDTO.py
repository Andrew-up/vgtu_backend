from model.model import ResultPredict


class ResultPredictDTO(object):

    def __init__(self, **entries):
        self.id_category = None
        self.name_category_eng = None
        self.name_category_ru = None
        self.__dict__.update(entries)

    def getResultPredict(self):
        model = ResultPredict()
        model.id_category = self.id_category
        model.name_category_eng = self.name_category_eng
        model.name_category_ru = self.name_category_ru
        return model

    def getDto(self):
        dto = ResultPredictDTO()
        dto.id_category = self.id_category
        dto.name_category_eng = self.name_category_eng
        dto.name_category_ru = self.name_category_ru
        return dto
