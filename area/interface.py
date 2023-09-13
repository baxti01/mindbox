from abc import ABC, abstractmethod


class BaseFigure(ABC):
    @abstractmethod
    def get_area(self, *args):
        raise NotImplemented
