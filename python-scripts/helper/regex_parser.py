import re
from pyquery import PyQuery
from typing import List

class RegexParser:
    """
    Static class for searching and parsing regular expressions in a pdf file
    """
    @staticmethod
    def parse_calendarWeek(file):
        """
        Searches current file for all LTTTextBoxHorizontal elements, that contain the string "Kalenderwoche". The string
        gets split up and the value of the week number gets extracted.

        Returns
        -------
        week number: str
        """
        return file.pq('LTTextBoxHorizontal:contains("Kalenderwoche:")').text() \
            .replace("Kalenderwoche: ", "", 1).split(" Datum")[0]

    @staticmethod
    def get_coordinates_of_weekday(file, weekday):
        """
        Search bbox of specific weekday and parse string into a list of floats
        """
        weekday_information = RegexParser.get_bbox_of_weekday(file, weekday)
        return (list(map(float, weekday_information.replace("[", "").replace(",", "").replace("]", "")
                         .split(" "))))

    @staticmethod
    def get_bbox_of_weekday(file, weekday):
        """
        Get bbox of weekday from file and return it as string
        """
        return file.pq('LTRect:contains(' + weekday + ')').attr["bbox"]

    @staticmethod
    def get_bbox_of_modules(file):
        """
        Method searches for all horizontal lines bigger than the standard date line

        Currently not in use, used and implemented on a different branch

        Returns
        -------
        String of bbox in form "[0, 0, 0 ,0]"
        """
        information_string = str(file.pq("LTLine:not(empty)").filter(lambda i, this: float(PyQuery(this).width()) > 100))
        return re.findall("\[(\d+\.\d+), (\d+\.\d+), (\d+\.\d+), (\d+\.\d+)\]", information_string)

    @staticmethod
    def get_current_year(file):
        """
        Searches year from current page
        """

        information_string = file.pq('LTTextBoxHorizontal:contains("Kalenderwoche: ")').text()
        years = [int(x)+2000 for x in re.findall("\/([0-9]*) bis (?:.*)?\/([0-9]*)", information_string)[0]]
        return years

    @staticmethod
    def extract_coordinates_from_bbox(pyQuery) -> List[float]:
        """
        Method extracts coordinates of PyQuery object

        Returns
        -------
        list(float) :  coordinates of box
        """
        string_without_brackets = re.sub("(['\s\(\)\[\]])", "",
                                         str(re.findall("\[(\d+\.\d+), (\d+\.\d+), (\d+\.\d+), (\d+\.\d+)\]",
                                                        str(pyQuery).split(">")[0])))

        return RegexParser.string_array_to_float_array(string_without_brackets)

    @staticmethod
    def extract_modules_pyquery_array(file, max_value, min_value):
        """
        Method extracts all lines bigger than the standard date line

        Returns
        -------
        PyQuery Object
        """
        return file.pq("LTLine").filter(lambda i, this: max_value > float(PyQuery(this).width()) > min_value)

    @staticmethod
    def string_array_to_float_array(string_without_brackets: str):
        return [float(value) for value in string_without_brackets.split(",")]

    @staticmethod
    def check_for_hyphen(item_as_string):
        """Some pages contain a '-' to indicate a range between weeks, this function is used to split them and fill
        fill the weeks with the missing numbers
        """
        int_array = list()
        # split string
        hyphen_list = list(map(int, item_as_string.split('-')))
        # check if string contained '-'
        if len(hyphen_list) > 1:
            # fill missing week numbers into the array from e.g 15-18: fill weeks 16, 17
            int_array += [int(x) for x in range(hyphen_list[0], hyphen_list[1]+1)]
        else:
            int_array.append(int(item_as_string))
        return int_array