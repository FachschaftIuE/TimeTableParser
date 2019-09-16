import csv
import pytz
import json
from ics import Calendar, Event
from datetime import datetime
from classes.data_item import DataItem
from typing import List
import pathlib

output_folder = pathlib.Path.cwd().joinpath('data', 'output')
cache_folder = pathlib.Path.cwd().joinpath('data', 'cache')

def create_csv(data: List[DataItem], filename: str = "calendar"):

    """
    Summary
    -------
    Parsing a list with data objects (DataItem) in a .csv-format and saves it in data/output.

    Parameter
    ---------
    data : list         # DataItem-list with events
    filename : str      # .csv-filename (default: calendar)
    """

    head_row = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Description', 'Location']
    filename = filename + '.csv'

    # Create .csv-file
    with open(output_folder.joinpath(filename), 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(head_row)

        # Every event has one row
        for event in data:
            writer.writerow([
                event.module,
                event.start_datetime.strftime("%d.%m.%Y"),
                event.start_datetime.strftime("%H:%M"),
                event.end_datetime.strftime("%d.%m.%Y"),
                event.end_datetime.strftime("%H:%M"),
                event.lecturer,
                event.location
            ])

    csv_file.close()


def create_ics(data: List[DataItem], filename: str = "calendar"):

    """
    Summary
    -------
    Parsing a list with data objects (DataItem) in a .ics-format and saves it in data/output.

    Parameter
    ---------
    data : list         # DataItem-list with events
    filename : str      # .csv-filename (default: calendar)
    """

    c = Calendar()

    for event in data:
        # converting start date, end date and time in order to get reccognized by ics-library
        start_date = datetime(year=int(event.start_datetime.year),
                              month=int(event.start_datetime.month),
                              day=int(event.start_datetime.day),
                              hour=int(event.start_datetime.hour),
                              minute=int(event.start_datetime.minute),
                              second=int(event.start_datetime.second)).astimezone(pytz.timezone('Europe/Berlin'))

        end_date = datetime(year=int(event.end_datetime.year),
                            month=int(event.end_datetime.month),
                            day=int(event.end_datetime.day),
                            hour=int(event.end_datetime.hour),
                            minute=int(event.end_datetime.minute),
                            second=int(event.end_datetime.second)).astimezone(pytz.timezone('Europe/Berlin'))

        # Create event and fill with event data
        e = Event()
        e.name = event.module
        e.begin = start_date
        e.end = end_date
        e.location = event.location
        e.description = event.lecturer

        # Add event to calendar
        c.events.add(e)

    filename = filename + '.ics'

    # Create .ics-file
    with open(output_folder.joinpath(filename), 'w', newline='', encoding='utf-8') as ics_file:
        ics_file.writelines(c)


def create_json(data: str, filename: str):
    """
    Summary
    -------
    Writing a JSON string to a .json file in data/output.

    Parameter
    ---------
    data : str          # json string
    filename : str      # .json-filename
    """

    # Throws an exception if the data is invalid JSON
    json.loads(data)

    filename = filename + '.json'

    # Create .json-file
    with open(cache_folder.joinpath(filename), 'w', newline='', encoding='utf-8') as json_file:
        json_file.writelines(data)

    json_file.close()


def create_json_from_data_item(data_item_list: List[DataItem], filename):
    filename = filename + '.json'

    with open(cache_folder.joinpath(filename), 'w', newline='', encoding='utf-8') as json_file:
        json_file.writelines('[')

        temp_list = list()

        # Create file from list
        for x in range(len(data_item_list)):
            if data_item_list[x].pdf_name == filename:
                temp_list.append(data_item_list[x])

        for x in range(len(temp_list)):
            json_file.writelines(temp_list[x].to_json())
            if x < (len(temp_list)-1):
                json_file.writelines(',')
        json_file.writelines(']')









