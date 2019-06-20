from classes.timetable_parts.timetable_part import TimetablePart
from datetime import date


class Day(TimetablePart):
    """
    Day-Object class to save all modules for corresponding day
    Class Arguments
    ---------------
    modules : list          # list of modules on specific day
    """
    modules = list()

    def __init__(self, date_of_day: date):
        super().__init__(date_of_day)
        self.date_of_day = date_of_day

    def calculate(self):
        """
        Implementation of abstract method, currently not in use
        """
        pass