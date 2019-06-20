from abc import ABC
from datetime import date


class TimetablePart(ABC):

    """
    Abstract class where Week and Day inherit from
    """
    start_date = None

    def __init__(self, start_date: date):
        self.start_date = start_date

    def calculate(self):
        """
        Abstract function, to realize composite pattern, currently not implemented
        """
        raise NotImplementedError("Not implemented")