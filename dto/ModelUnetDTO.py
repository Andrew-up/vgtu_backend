from model.model import ModelUnet
class ModelUnetDTO(object):

    def __init__(self, **entries):
        self.id = None
        self.version = None
        self.accuracy = None
        self.date_train = None
        self.quality_dataset = None
        self.quality_train_dataset = None
        self.quality_valid_dataset = None
        self.current_epochs = None
        self.total_epochs = None
        self.time_train = None
        self.num_classes = None
        self.input_size = None
        self.output_size = None
        self.status = None
        self.__dict__.update(entries)

    def getDTO(self):
        dto = ModelUnetDTO()
        dto.id = self.id
        dto.version = self.version
        dto.accuracy = self.accuracy
        dto.date_train = self.date_train
        dto.quality_dataset = self.quality_dataset
        dto.quality_train_dataset = self.quality_train_dataset
        dto.quality_valid_dataset = self.quality_valid_dataset
        dto.current_epochs = self.current_epochs
        dto.total_epochs = self.total_epochs
        dto.time_train = self.time_train
        dto.num_classes = self.num_classes
        dto.input_size = self.input_size
        dto.output_size = self.output_size
        dto.status = self.status
        return dto

    def getModelUnet(self) -> ModelUnet:
        model_unet = ModelUnet()
        model_unet.id = self.id
        model_unet.version = self.version
        model_unet.accuracy = self.accuracy
        model_unet.date_train = self.date_train
        model_unet.quality_dataset = self.quality_dataset
        model_unet.quality_train_dataset = self.quality_train_dataset
        model_unet.quality_valid_dataset = self.quality_valid_dataset
        model_unet.current_epochs = self.current_epochs
        model_unet.total_epochs = self.total_epochs
        model_unet.time_train = self.time_train
        model_unet.num_classes = self.num_classes
        model_unet.input_size = self.input_size
        model_unet.output_size = self.output_size
        model_unet.status = self.status
        return model_unet
