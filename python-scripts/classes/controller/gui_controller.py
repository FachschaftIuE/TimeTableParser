from tkinter import messagebox

from classes.controller.timetable_controller import TimetableController
from classes.file_management.loader import Loader
from classes.models.timetable import Timetable
from classes.view import gui
from helper.data_handler import get_module_names_from_data_items
from helper.data_output import create_ics, create_csv, create_json_from_data_item
from helper.folder_manager import path_leaf, get_cached_file_for
from helper.get_pdf_pages import count_pdf_pages


class GuiController:

    def __init__(self):
        self.files = []
        self.selectable_modules = []
        self._parsed_data_items = []

    def clear_inputs(self):
        self.files.clear()
        self.selectable_modules.clear()
        self._parsed_data_items.clear()

    def create_calendar(self, agreed_to_tos, export_as_ics, selected_module_indices):
        if not agreed_to_tos:
            messagebox.showerror(gui.title, "You need to agree to the Terms Of Service to do that.")
            return

        if len(self._parsed_data_items) == 0:
            messagebox.showinfo(gui.title, "There are no modules to select.\nPlease parse a timetable.")
            return

        if len(selected_module_indices) == 0:
            messagebox.showinfo(gui.title, "There are no modules selected.\n"
                                           "Please select modules to fill the calendar with.")
            return

        selected_module_names = []
        for index in selected_module_indices:
            selected_module_names.append(self.selectable_modules[index])

        selected_modules = []
        for data_item in self._parsed_data_items:
            if selected_module_names.__contains__(data_item.module):
                selected_modules.append(data_item)

        if export_as_ics:
            create_ics(selected_modules)
        else:
            create_csv(selected_modules)

        messagebox.showinfo(gui.title, "Created the calendar. Check the /data/output folder! 😊")

    def parse_inputs(self, use_cache, agreed_to_tos):
        if not agreed_to_tos:
            messagebox.showerror(gui.title, "You need to agree to the Terms Of Service to do that.")
            return

        if len(self.files) == 0:
            messagebox.showinfo(gui.title, "There are no timetables to parse. "
                                           "To parse a timetable add it via the 'Add Timetable'-Button.")
            return

        # reset from previous parse
        self.selectable_modules = []
        self._parsed_data_items = []

        messagebox.showinfo(gui.title, "This process may take a while. Grab a something to drink! 😊")

        for file in self.files:
            # try:
                cached_file = get_cached_file_for(path_leaf(file))
                file_is_parsed_already = cached_file.is_file()

                data_items_in_file = get_data_items_from_file(cached_file) if file_is_parsed_already and use_cache \
                    else get_data_items_from_file(file)

                for data_item in data_items_in_file:
                    self._parsed_data_items.append(data_item)

                modules_in_data_items = get_module_names_from_data_items(data_items_in_file)
                for module in modules_in_data_items:
                    self.selectable_modules.append(module)

                if not (file_is_parsed_already and use_cache):
                    create_json_from_data_item(data_items_in_file, path_leaf(cached_file).replace('.json', ''))
                print(path_leaf(file) + " was successfully parsed.")

            # except Exception as e:    # TODO catch in production
            #     messagebox.showerror(gui.title, "Couldn't parse the timetable '"+path_leaf(file)+"' because:\n"+str(e))

        messagebox.showinfo(gui.title, "Parsing finished! 😊")


def get_data_items_from_file(file):

    """
    Summary
    -------
    Retrieves the data items from the given file.

    Parameter
    ---------
    file : path                 # Absolute path of the file that's going to be parsed.
                                  Supports *.json and *.pdf files.
    timetable : timetable       # The timetable to retrieve the info with.
    """

    data_items = []

    if str(file).endswith('.pdf'):
        timetable = Timetable()

        page_count = count_pdf_pages(file)
        for page_index in range(page_count):
            timetable_controller = TimetableController(Loader(file, path_leaf(file), page_index), timetable)
            timetable_controller.create_timetable_information()
            timetable_controller.send_data_to_timetable()
            timetable.search_modules()
            timetable.get_weeks()
            timetable.find_modules(data_items)

    else:
        pass    # TODO implement

    # try:
    #     files = file_handler(convert_files(self.files, '.pdf'), read_cache_folder(), use_cache)
    #
    #     for file_index in range(files["files_to_parse"].__len__()):
    #         page_count = get_pdf_pages(files["files_to_parse"][file_index]["file_path"])
    #
    #         for page in range(page_count):
    #             file_container = Loader(files["files_to_parse"][file_index]["file_path"],
    #                                     files["files_to_parse"][file_index]["file_name"],
    #                                     page)
    #
    #             timetable = Timetable()
    #             t_controller = TimetableController(file_container, timetable)
    #             t_controller.create_timetable_information()
    #             t_controller.send_data_to_timetable()
    #             timetable.search_modules()
    #             timetable.get_weeks()
    #             timetable.find_modules(self._parsed_data_items)
    #
    #         create_json_from_data_item(self._parsed_data_items, files["files_to_parse"][file_index]["file_name"])
    #
    #     for file_index in range(files["files_to_load"].__len__()):
    #         data_item_from_json(self._parsed_data_items, files["files_to_load"][file_index]["file_path"])
    #
    #     for data_item in create_data_dictionary(self._parsed_data_items):
    #         self.selectable_modules.append(data_item)
    #
    #
    #
    # except Exception as e:
    #     messagebox.showerror(gui.title, "Could not parse the timetable because:\n" + str(e))

    return data_items
