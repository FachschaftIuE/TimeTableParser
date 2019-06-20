from helper.regex_parser import RegexParser

class TimetableInformation:
    """
    Container Object for all basic Information to corresponding timetable

    Class Args
    ----------
    week_day_information:       Dict(Day)
    time_stamp_information:     Dict(float)     # Key = "8:30", "8:45" etc.
    total_pages:                int
    week_numbers:               list(int)
    current_year:               int
    week_days_per_week:         list(str)       # Information which days are contained in week i.e. ["Mo", "Di", "Mi"]
    single_time_stamp_width     float           # Width of a single time stamp, needed to calculate coordinates of timestamps
    """

    def __init__(self):
        self.week_day_information = dict()
        self.time_stamp_information = dict()
        self.total_pages = 0
        self.week_numbers = list()
        self.current_year = list()
        self.week_days_per_week = list()
        self.single_time_stamp_width = 0

    # Setter
    def set_week_day_information(self, week_day_information: dict):
        self.week_day_information = week_day_information

    def set_time_stamp_information(self, time_stamp_information: dict):
        self.time_stamp_information = time_stamp_information

    def set_total_pages(self, total_pages: int):
        self.total_pages = total_pages

    def set_week_numbers(self, week_numbers: str):
        # parse list of lists, to list of ints
        helper_list = week_numbers.split(',')
        for item in helper_list:
            # split item into string to check for hyphen
            self.week_numbers += RegexParser.check_for_hyphen(item)

    def set_current_year(self, current_year):
        self.current_year = current_year

    def set_week_days_per_week(self, week_days_per_week: list):
        self.week_days_per_week = week_days_per_week

    def set_single_time_stamp_width(self, single_time_stamp_width):
        self.single_time_stamp_width = single_time_stamp_width
