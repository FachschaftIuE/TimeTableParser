import datetime

from classes.file_management.loader import Loader
from classes.timetable_parts.week import Week
from helper.data_handler import create_event, string_to_datetime
from helper.regex_parser import RegexParser
from .event_meta import EventMeta
from .iterable import *
from .timetable_information import TimetableInformation


class Timetable:
    """
       Summary
       -------
       Timetable data object

       Parameter
       ---------
       __timetable_information : TimetableInformation    # Base information of current timetable
       __loader :                Loader                  # Instance of Loader class. @see loader.py for more
                                                         information
       __weeks :                 Dict(Week)              # Dictionary of weeks contained in this timetable,
                                                         Key = Week number, value = Week
       """
    __timetalbe_information = None
    __loader = None
    __weeks = None
    __modules = list()

    def set_data(self, timetalbe_information: TimetableInformation, loader: Loader):
        """
        Data gets compiled in TimetableController. Afterwards the data(TimetableInformation) gets send to the Timetable
        class, containing basic information.
        """
        self.__timetalbe_information = timetalbe_information
        self.__loader = loader
        self.__word_margin = float(self.__loader.get_file().pq('LTTextLineHorizontal').attr["word_margin"])

    def search_modules(self):
        test_list = RegexParser.get_bbox_of_modules(self.__loader.get_file())

    def get_weeks(self):
        """
        Searches the loaded file and replaces/deletes certain expressions for a more readable format.
        """
        calendar_numbers = RegexParser.parse_calendarWeek(self.__loader.get_file())
        self.__timetalbe_information.set_week_numbers(calendar_numbers)
        self.__fill_weeks()

    def __calculate_date_from_week_number(self, week_number):
        """
        Function gets passed a week number and calculates the start date of the week
        Returns
        -------
        String of current date in format YYYY-MM-DD
        """

        total_weeks = self.__get_total_weeks_of_year()
        # Gets from - to - years, can differ in the winter semester
        years = self.__timetalbe_information.current_year
        date = ""

        # Check if years correspond or if there are multiple years on one page
        if years[0] == years[1]:
            date = str(self.__timetalbe_information.current_year[0]) + "-W" + str(week_number)

            # Check if week number is greater than all weeks in the year.
            if week_number > total_weeks:
                week_number = week_number % total_weeks
                date = str(self.__timetalbe_information.current_year[1]) + "-W" + str(week_number)

        # Catches the case, that there are multiple years on one page. Currently not happened
        else:
            if week_number > total_weeks:
                week_number = week_number % total_weeks
                date = str(self.__timetalbe_information.current_year[1]) + "-W" + str(week_number)

        # Returns date string
        return datetime.datetime.strptime(date + '-1', "%G-W%V-%u")

    # Check if year has 52 or 53 weeks
    def __get_total_weeks_of_year(self):
        gemein_jahre = [2020, 2026, 2032, 2037]
        total_weeks = 52
        if self.__timetalbe_information.current_year[0] - 1 in gemein_jahre:
            total_weeks = 53
        return total_weeks

    def __fill_weeks(self):
        """
        Method iterates over dictionary and searches start date for every week and passes start date to week Object
        """
        self.__weeks = dict()
        for week in self.__timetalbe_information.week_numbers:
            self.__weeks[str(week)] = (Week(self.__calculate_date_from_week_number(week), week)
                                       .fill_days(self.__timetalbe_information.week_days_per_week))

    def find_modules(self, data: list):
        """
        This method was made with not a lot of style guides in mind, as you probably can see. There was no time left to
        structure this part of the code better. Hopefully the comments will help future generations to improve this mess.
        We are truly sorry mv&gp
        """

        # test is a list of all horizontal lines bigger than the default date (sorry for the variable naming)
        test = RegexParser.extract_modules_pyquery_array(self.__loader.get_file(),
                                                         (self.__timetalbe_information.single_time_stamp_width *
                                                          len(self.__timetalbe_information.time_stamp_information)),
                                                         self.__timetalbe_information.single_time_stamp_width)

        module_events = list()
        event_meta_list = list()

        for i in test.items():
            module_events.append(RegexParser.extract_coordinates_from_bbox(i))

        for beam in module_events:
            # we give the elements a boolean, to avoid handling them twice, see below
            beam.append(True)

        # we iterate over all weekdays on the current page
        for key, value in self.__timetalbe_information.week_day_information.items():
            # indexes for the elements: 0 => x0, 1 => y0, 2 => x1, 3 => y1, 4 => boolean (not processed == True)
            # we need to determine the height of a weekday to check for corresponding beams
            day_height = value[3] - value[1]
            for event in module_events:
                if not (event[1] == value[3] and event[4]):
                    # we skip if the beam (event) doesn't match up with the weekday and has not been processed (kill me)
                    continue
                for other_event in module_events:
                    # if both events have the same length and the other event hasn't been processed yet
                    if (event[0] == other_event[0]) and (event[2] == other_event[2]) and (other_event[4]):
                        # and the events are day_height apart on the y-axis
                        if event[1] - day_height == other_event[1]:
                            # we recognize those coordinates as an event
                            event_meta_list.append(EventMeta(key, event[0], event[2]))
                            # and set the 'not processed-flag' to false
                            event[4] = False
                            other_event[4] = False
                            # anybody still paying attention?
                            break

        # Iterate over all boxes and find module names, rooms and prof names
        for item in event_meta_list:
            module_information = self.__find_module_info(item.day_name, item.get_box())

            # Iterate over dictionary, because one page can contain multiple weeks. Sorry for the naming
            for key, value in self.__weeks.items():
                # Get current date of day
                start_date = value.days[item.day_name].date_of_day.strftime("%d/%m/%Y")
                start_end_time = self.__find_module_time(item)
                create_event(data, self.__loader.get_file_name(), module_information["Module"].content,
                             string_to_datetime(start_date, start_end_time["start"]),
                             string_to_datetime(start_date, start_end_time["end"]),
                             module_information["Prof"].content, module_information["Room"].content)

    def __find_module_time(self, item):

        return_information = {"start": "", "end": ""}

        # Iterate over dictionary to find x0 and x1 value of timestamp
        for time, tuple in self.__timetalbe_information.time_stamp_information.items():

            # Check for beginning time
            if round(tuple[0], 2) == round(item.x0, 2):
                return_information["start"] = time

            # Check for end time
            if round(tuple[0], 2) == round(item.x1, 2):
                return_information["end"] = time

        # Return dictionary with ["end" : "end time", "start" : "start time"]
        return return_information

    def __find_module_info(self, week_day_name: str, box: Box):

        module_name_box = list()

        # Definition of outer box, which contains strings
        main_box = Box(
            [box.x0, self.__timetalbe_information.week_day_information[week_day_name][1] - self.__word_margin,
             box.x1, self.__timetalbe_information.week_day_information[week_day_name][3]])

        m_name_finder_initializer = ModuleNameFinder(main_box)
        m_name_finder_initializer.min_box = main_box
        # Find module names
        m_name_finder = self.__iterator(m_name_finder_initializer)

        m_prof_finder = ModuleProfFinder(main_box)
        m_prof_finder.module_name_box = m_name_finder.content_box

        # Find prof names
        self.__iterator(m_prof_finder)

        m_room_finder = ModuleRoomFinder(main_box)
        m_room_finder.module_name_box = m_name_finder.content_box
        m_room_finder.min_box = m_name_finder.min_box

        # Find room names
        self.__iterator(m_room_finder)

        return {"Module": m_name_finder, "Room": m_room_finder, "Prof": m_prof_finder}

    def __iterator(self, iterable: Iterable):
        """
        Method gets passed an Iterable (@see iterable.py) and executes its method. This pattern helps to use only one
        for loop, not three
        """
        # Iterate over PyQuery-Items
        for item in self.__loader.get_file().pq('LTTextLineHorizontal:in_bbox("'
                                                + str(iterable.main_box.x0) + ', ' + str(iterable.main_box.y0) + ','
                                                + str(iterable.main_box.x1) + ', '
                                                + str(iterable.main_box.y1) + '")').items():
            description_box = Box(RegexParser.extract_coordinates_from_bbox(item))
            iterable.get_information(BoxContent(description_box, item.text()))

        return iterable
