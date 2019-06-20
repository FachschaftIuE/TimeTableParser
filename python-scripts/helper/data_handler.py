from classes.data_item import DataItem
from classes.dictionary_item import DictionaryItem
from typing import List
from datetime import datetime


def create_event(data: List[DataItem], pdf_name: str, module: str, start_datetime: datetime, end_datetime: datetime,
                 lecturer: str, location: str):

    """
    Summary
    -------
    Replace the default constructor from data_item/DataItem.
    Extra functionalities:  - Adds new event directly to DataItem-list
                            - Sets unique module id for every module type in DataItem-list

    Parameter
    ---------
    data : list                 # DataItem-list with events
    pdf_name : str              # name from parsed pdf
    module : str                # module name
    start_datetime : datetime   # start datetime
    end_datetime : datetime     # end datetime
    lecturer : str              # lecturer name
    location : str              # building & room number
    """

    new_event = DataItem(pdf_name, module, start_datetime, end_datetime, lecturer, location)

    module_id = 0

    for event in data:
        if new_event.module_id == -1:
            if event.module == new_event.module and event.pdf_name == new_event.pdf_name:
                new_event.set_module_id(event.module_id)
                break

        if event.module_id >= module_id:
            module_id = event.module_id

    if new_event.module_id == -1:
        new_event.set_module_id((module_id + 1))

    data.append(new_event)


def string_to_datetime(date: str, time: str):

    """
    Summary
    -------
    Combine date and time string to datetime.

    Parameter
    ---------
    date : str    # date    (Format: DD/MM/YYYY)
    time : str    # time    (24h Format: 00:00)

    See Also
    --------
    datetime :      Output with point-operator.
                    Keywords: year, month, day, hour, minute, second
                    Example:  datetime.hour
    """

    temp_date = date.split('/')
    temp_time = time.split(':')

    temp_datetime = datetime(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]),
                             int(temp_time[0]), int(temp_time[1]), 00)

    return temp_datetime


def create_data_dictionary(data: List[DataItem]):

    """
    Summary
    -------
    Creates a dictionary list from DataItem-list and returns it.
    One entry for every module type.

    Parameter
    ---------
    data : list         # DataItem-list with events

    Returns
    -------
    dictionary : list   # DictionaryItem-list with module id, module name and pdf name
    """

    dictionary = list()

    for event in data:
        if len(dictionary) > 0:

            entry_exists = 0

            for entry in dictionary:
                if entry.module_id == event.module_id:
                    entry_exists = 1
            if entry_exists == 0:
                dictionary.append(DictionaryItem(event))
            else:
                entry_exists = 0
        else:
            dictionary.append(DictionaryItem(event))

    return dictionary


def filter_data_list(data: List[DataItem], whitelist_ids: List[int]):

    """
    Summary
    -------
    Removes all events in DataItem-list which are not included in whitelist.

    Parameter
    ---------
    data : list             # DataItem-list with events
    whitelist_ids : list    # int-list (module_id) with whitelisted modules
    """

    if len(whitelist_ids) == 0:
        data.clear()
        return

    temp_data = list()

    for event in data:

        for wl_id in whitelist_ids:

            if wl_id == event.module_id:
                temp_data.append(event)
                break

    data.clear()

    for temp_event in temp_data:
        data.append(temp_event)
