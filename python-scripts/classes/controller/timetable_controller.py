from classes.file_management.loader import Loader
from helper.regex_parser import RegexParser
from classes.models.timetable_information import TimetableInformation
from classes.models.timetable import Timetable


class TimetableController:
    """
    Controller to fill TimetableInformation-Object with basic information e.g. Days in Week, width of timestamp etc.

    Class Args
    ----------
    __timetable_information:            TimetableInformation    # Container where all information is stored
                                                                @see timetable_information.py for more information
    __week_day_info:                    Dict(Day)               #
    __time_stamp_info:                  Dict(float)
    __offset_time_stamp:                float                   # Left offset of time_stamp, needed to calculate
                                                                position of other timestamps. Is needed because not all
                                                                lines of the timestamps in the pdf can be read, only
                                                                the first one.
    __time_stamp_width:                 float                   # Width of the first time_stamp_line
    __time_stamp_height:                float                   # Height of the first time_stamp_line
    __week_day_names:                   List(str)               # Contains all weekdays as string
    __time_stamps:                      List(str)               # All time_stamps on a single timetable page. If other
                                                                timestamps appear in the timetable, just insert them in
                                                                following manner: hh:mm
    __loader:                           Loader                  # Instance of Loader class. @see loader.py for more
                                                                information
    """
    __timetable_information = None
    __week_day_info = dict()
    __time_stamp_info = dict()
    __offset_time_stamp = 0
    __time_stamp_width = 0
    __time_stamp_height = 0
    __week_day_names = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    __time_stamps = ["8:30", "8:45", "9:00", "9:15", "9:30", "9:45", "10:00", "10:15", "10:30", "10:45", "11:00",
                        "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30",
                        "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00",
                        "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30",
                        "18:45", "19:00", "19:15", "19:30", "19:45", "20:00"]

    def __init__(self, loader: Loader, timetable: Timetable):
        self.__loader = loader
        self.__timetable = timetable

        # Check if week consist of seven days, otherwise remove day from list
        for day in reversed(self.__week_day_names):
            if RegexParser.get_bbox_of_weekday(self.__loader.get_file(), day) is None:
                self.__week_day_names.remove(day)
        self.__get_time_stamp_data_for_calculation()
        self.__initialize_coordinates_of_time_stamps()
        self.__get_days()

    def send_data_to_timetable(self):
        self.__timetable.set_data(self.__timetable_information, self.__loader)

    def __get_time_stamp_data_for_calculation(self):
        """
        Searches for the first time stamp 8:30 and saves its width, offset and height for later calculation

        Returns
        -------
        self: Loader
            returns reference for chaining
        """
        lt_rect_object = self.__loader.get_file().pq('LTRect:contains(\'' + self.__time_stamps[0] + '\')')
        self.__time_stamp_width = float(lt_rect_object.attr["width"])
        self.__offset_time_stamp = lt_rect_object.attr["x0"]
        self.__time_stamp_height = lt_rect_object.attr["height"]

    def __initialize_coordinates_of_time_stamps(self):
        """
        Iterates over every time stamp and calculates its x-position and adds the information to a list

        Returns
        -------
        None
=        """
        for x in range(1, len(self.__time_stamps) + 1):
            # Round on three digits, for better calculation
            self.__time_stamp_info[self.__time_stamps[x - 1]] = (round((float(self.__offset_time_stamp) +
                                                                        (x - 1) * float(self.__time_stamp_width)), 3),
                                                                 round((float(self.__offset_time_stamp) +
                                                                       x * float(self.__time_stamp_width)), 3))
    def __get_days(self):
        """
        Method searches in file for the specified weekday and returns the attribute 'bbox' which contains x and y
        coordinates for the weekdays.

        Parameters
        ----------
        weekday: str
            Name of the weekday as string, in form Mo, Di, Mi etc.

        Returns
        -------
        None
        """
        for weekday in self.__week_day_names:
            self.__week_day_info[weekday] = RegexParser.get_coordinates_of_weekday(self.__loader.get_file(), weekday)

    def create_timetable_information(self):
        """
        Creates TimetableInformation-Objects and sets data
        """
        self.__timetable_information = TimetableInformation()
        self.__timetable_information.set_time_stamp_information(self.__time_stamp_info)
        self.__timetable_information.set_week_day_information(self.__week_day_info)
        self.__timetable_information.set_total_pages(self.__loader.get_file().doc.catalog['Pages'].resolve()['Count'])
        self.__timetable_information.set_week_days_per_week(self.__week_day_names)
        self.__timetable_information.set_current_year(RegexParser.get_current_year(self.__loader.get_file()))
        self.__timetable_information.set_single_time_stamp_width(self.__time_stamp_width)