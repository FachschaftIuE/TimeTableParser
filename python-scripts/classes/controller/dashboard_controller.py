import ntpath
from tkinter import messagebox

from classes.controller.timetable_controller import TimetableController
from classes.file_management.loader import Loader
from classes.models.timetable import Timetable
from classes.view import gui
from helper.data_item_from_json import data_item_from_json
from helper.data_output import create_json_from_data_item
from helper.get_pdf_pages import get_pdf_pages


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class GuiController:

    def __init__(self):
        self.files = []

    def clear_inputs(self):
        self.files.clear()

    def parse_inputs(self, use_cache, export_as_ics, tos):
        if not tos:
            messagebox.showerror(gui.title, "You need to agree to the Terms Of Service to do that.")
            return

        if len(self.files) == 0:
            messagebox.showinfo(gui.title, "There are no timetables to parse. "
                                           "To parse a timetable add it via the 'Add Timetable'-Button.")
            return

        messagebox.showinfo(gui.title, "This process may take a while. Grab a something to drink! 😊")

        data = self.create_and_cache_json()

        for file in self.files:
            data_item_from_json(data, file)

        messagebox.showinfo(gui.title, "Done parsing! 😊")

    def create_and_cache_json(self):
        data = list()
        for file in self.files:
            page_count = get_pdf_pages(file)

            for page in range(page_count):
                file_container = Loader(file, path_leaf(file), page)

                timetable = Timetable()
                t_controller = TimetableController(file_container, timetable)
                t_controller.create_timetable_information()
                t_controller.send_data_to_timetable()
                timetable.search_modules()
                timetable.get_weeks()
                timetable.find_modules(data)

            create_json_from_data_item(data, file)
        return data

