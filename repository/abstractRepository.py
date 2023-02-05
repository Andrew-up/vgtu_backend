import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self,  id_item: int):
        raise NotImplementedError

