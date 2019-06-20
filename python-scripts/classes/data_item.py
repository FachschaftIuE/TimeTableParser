from datetime import datetime


class DataItem(object):

    """
    Summary
    -------
    Data object for one event.

    Parameter
    ---------
    module : str            # module name
    start_datetime : str    # start datetime
    end_datetime : str      # end datetime
    lecturer : str          # lecturer name
    location : str          # building & room number
    pdf_name : str          # name from parsed pdf

    See Also
    --------
    start_datetime, end_datetime :  Output with point-operator.
                                    Keywords: year, month, day, hour, minute, second
                                    Example: start_datetime.hour
    module_id :                     set from data_handler.create_event to group events by module name
    """

    module_id: int              # module id to group same modules
    module: str                 # module name
    start_datetime: datetime    # start date & time
    end_datetime: datetime      # end date & time
    lecturer: str               # lecturer name
    location: str               # building & room number
    pdf_name: str               # pdf name

    def __init__(self, pdf_name: str, module: str, start_datetime: datetime, end_datetime: datetime,
                 lecturer: str, location: str):

        self.module_id = -1
        self.module = module
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.lecturer = lecturer
        self.location = location
        self.pdf_name = pdf_name

    def set_module_id(self, module_id: int):

        self.module_id = module_id

    def print(self):

        print("[ " + self.pdf_name + " | " + self.module_id.__str__() + " | " + self.module + " | "
              + self.start_datetime.strftime("%d.%m.%Y , %H:%M") + " | "
              + self.end_datetime.strftime("%d.%m.%Y , %H:%M") + " | "
              + self.lecturer + " | " + self.location + " ]")

    def to_json(self):

        return "{" \
               "\"__DataItem__\" : true," \
               "\"module\" : \"" + self.module + "\"," \
               "\"start_datetime\" : \"" + str(self.start_datetime) + "\", " \
               "\"end_datetime\" : \"" + str(self.end_datetime) + "\", " \
               "\"lecturer\" : \"" + self.lecturer + "\", " \
               "\"location\" : \"" + self.location + "\", " \
               "\"pdf_name\" : \"" + self.pdf_name + "\"" \
                "}"
