from tkinter import messagebox

from classes.controller.timetable_controller import TimetableController
from classes.file_management.loader import Loader
from classes.models.timetable import Timetable
from classes.view import gui
from helper.data_handler import create_data_dictionary
from helper.data_item_from_json import data_item_from_json
from helper.data_output import create_json_from_data_item
from helper.folder_manager import file_handler, read_cache_folder, convert_files
from helper.get_pdf_pages import get_pdf_pages


class GuiController:

    def __init__(self):
        self.files = []
        self.data_items = []

    def clear_inputs(self):
        self.files.clear()

    def create_calendar(self):
        pass  # TODO implement

    def select_data_item(self, event):
        pass  # TODO implement

    def deselect_data_item(self, event):
        pass  # TODO implement

    def parse_inputs(self, use_cache, export_as_ics, tos):
        if not tos:
            messagebox.showerror(gui.title, "You need to agree to the Terms Of Service to do that.")
            return

        if len(self.files) == 0:
            messagebox.showinfo(gui.title, "There are no timetables to parse. "
                                           "To parse a timetable add it via the 'Add Timetable'-Button.")
            return

        messagebox.showinfo(gui.title, "This process may take a while. Grab a something to drink! 😊")

        data = list()
        files = file_handler(convert_files(self.files, '.pdf'), read_cache_folder(), use_cache)

        for file_index in range(files["files_to_parse"].__len__()):
            page_count = get_pdf_pages(files["files_to_parse"][file_index]["file_path"])

            for page in range(page_count):
                file_container = Loader(files["files_to_parse"][file_index]["file_path"],
                                        files["files_to_parse"][file_index]["file_name"],
                                        page)

                timetable = Timetable()
                t_controller = TimetableController(file_container, timetable)
                t_controller.create_timetable_information()
                t_controller.send_data_to_timetable()
                timetable.search_modules()
                timetable.get_weeks()
                timetable.find_modules(data)

            create_json_from_data_item(data, files["files_to_parse"][file_index]["file_name"])

        for file_index in range(files["files_to_load"].__len__()):
            data_item = data_item_from_json(data, files["files_to_load"][file_index]["file_path"])

        for data_item in create_data_dictionary(data):
            self.data_items.append(data_item)

        # TODO convert to gui
        # filter_data_list(data, user_select(c))
        # format_select(data)

        messagebox.showinfo(gui.title, "Parsing finished! 😊")


