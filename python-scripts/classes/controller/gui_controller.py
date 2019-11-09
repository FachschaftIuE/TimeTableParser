from tkinter import messagebox

from classes.controller.timetable_controller import TimetableController
from classes.file_management.loader import Loader
from classes.models.timetable import Timetable
from classes.view import gui
from helper.data_handler import create_data_dictionary
from helper.data_item_from_json import data_item_from_json
from helper.data_output import create_json_from_data_item, create_ics, create_csv
from helper.folder_manager import file_handler, read_cache_folder, convert_files
from helper.get_pdf_pages import get_pdf_pages


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
            selected_module_names.append(self.selectable_modules[index].module)

        selected_modules = []
        for module in self._parsed_data_items:
            if selected_module_names.__contains__(module.module):
                selected_modules.append(module)

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

        # TODO fix parsing multiple files
        # TODO fix filepath issues when not from 'correct' folder

        # reset from previous parse
        self.selectable_modules = []
        self._parsed_data_items = []

        messagebox.showinfo(gui.title, "This process may take a while. Grab a something to drink! 😊")

        try:
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
                    timetable.find_modules(self._parsed_data_items)

                create_json_from_data_item(self._parsed_data_items, files["files_to_parse"][file_index]["file_name"])

            for file_index in range(files["files_to_load"].__len__()):
                data_item_from_json(self._parsed_data_items, files["files_to_load"][file_index]["file_path"])

            for data_item in create_data_dictionary(self._parsed_data_items):
                self.selectable_modules.append(data_item)

            messagebox.showinfo(gui.title, "Parsing finished! 😊")

        except Exception as e:
            messagebox.showerror(gui.title, "Could not parse the timetable because:\n" + str(e))


