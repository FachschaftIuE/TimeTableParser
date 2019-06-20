from classes.timetable_parts.timetable_part import TimetablePart
from classes.timetable_parts.day import Day
import datetime


class Week(TimetablePart):
    """
    Class to represent a Week in a timetable. Holds days corresponding to week
    Class Variables
    ---------
    days :        Dict(Day)        # dictionary containing all days as Day-Object, key = str: "Mo", "Di", "Mi" etc.
    week_number : int              # Number of current week
    """
    days = None
    week_number = 0

    def __init__(self, startdate: datetime.date, week_number: int):
        super().__init__(startdate)
        self.week_number = week_number

    def calculate(self):
        """
        Implementation of abstract method, currently not used.
        """
        for day in self.days:
            day.calculate()

    def fill_days(self, list_of_days: list):
        """
        Method calculates dates of Days in corresponding week and fills dictionary
        Params
        ------
        list_of_days : list(days)    # List of days to calculate date for
        Returns
        ------
        self : Week                  # return self for chaining
        """
        current_date = self.start_date
        self.days = dict()
        for day in list_of_days:
            self.days[day] = Day(current_date)
            current_date += datetime.timedelta(days=1)
        return self
