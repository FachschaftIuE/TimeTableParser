import json
from classes.data_item import DataItem
from datetime import datetime
from helper.data_handler import create_event


def decode_data_item(dct)->DataItem:
    """
    Summary
    -------
    Transforms a dictionary into DataItem objects.

    Parameter
    ---------
    dct : dct      # dictionary with decoded json values
    """

    if "__DataItem__" in dct:
        return DataItem(dct["pdf_name"], dct["module"],
                        datetime.strptime(dct["start_datetime"], '%Y-%m-%d %H:%M:%S'),
                        datetime.strptime(dct["end_datetime"], '%Y-%m-%d %H:%M:%S'),
                        dct["lecturer"], dct["location"])
    return dct


def data_item_from_json(data_item_list, filepath: str):
    """
    Summary
    -------
    Returns a list or a single DataItem object from a json file in the data/cache

    Parameter
    ---------
    filename : str      # .json-filename
    """

    with open(filepath, 'r', encoding="utf-8") as item_data:
        data = item_data.read()
        z = json.loads(data, object_hook=decode_data_item)

    for data_item in z:
        # TODO Search better way to create list of dataitems
        create_event(data_item_list, data_item.pdf_name, data_item.module, data_item.start_datetime,
                     data_item.end_datetime, data_item.lecturer, data_item.location)

