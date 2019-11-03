import tkinter as tk
from tkinter import filedialog

from classes.controller.dashboard_controller import GuiController, path_leaf

# constants
title = "TimeTableParser"
height = 650
width = 300


class Gui:
    controller = GuiController()
    root = tk.Tk()
    input_section = tk.Frame(root)
    input_files = tk.Frame(input_section)
    input_file_list = tk.Listbox(input_files, width=40)

    def __init__(self):
        self.root.title(title)
        self.center_window_on_screen()
        self.use_cache = tk.BooleanVar()
        self.export_as_ics = tk.BooleanVar()
        self.tos = tk.BooleanVar()

    def show(self):
        self.build_ui()
        self.root.mainloop()

    def add_file(self):
        filename = filedialog.askopenfilename(title="Select a Timetable", filetypes=[("Timetables", "*.pdf")])
        if filename != "" and not self.controller.files.__contains__(filename):
            self.controller.files.append(filename)
            self.refresh_inputs()

    def refresh_inputs(self):
        # clear listbox
        self.input_file_list.delete(0, tk.END)

        # add files
        for input_file in self.controller.files:
            self.input_file_list.insert(tk.END, path_leaf(input_file))

    def center_window_on_screen(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def build_ui(self):
        # region input section

        self.input_section.pack(pady=10)
        self.input_files.pack()

        # label
        input_file_label = tk.Label(self.input_files, text="TimeTables", font='Helvetica 10 bold')
        input_file_label.pack()

        # list of input files
        self.input_file_list.pack(side=tk.LEFT, fill=tk.BOTH)
        input_file_list_scrollbar = tk.Scrollbar(self.input_files)
        input_file_list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        input_file_list_scrollbar.config(command=self.input_file_list.yview)
        self.input_file_list.config(yscrollcommand=input_file_list_scrollbar.set)

        # input buttons
        input_section_buttons = tk.Frame(self.input_section)
        input_section_buttons.pack(side=tk.BOTTOM)
        clear_button = tk.Button(input_section_buttons, text="Clear",
                                 command=lambda: [self.controller.clear_inputs(), self.refresh_inputs()])
        clear_button.pack(side=tk.LEFT, padx=10)
        add_button = tk.Button(input_section_buttons, text="Add Timetable", command=self.add_file)
        add_button.pack(side=tk.RIGHT, padx=10)

        # endregion

        # region settings section
        settings_section = tk.Frame(self.root)
        settings_section.pack(pady=20)

        # label
        settings_label = tk.Label(settings_section, text="Settings", font='Helvetica 10 bold')
        settings_label.grid(row=0, column=0, columnspan=2)

        # checkboxes
        use_cache_checkbox = tk.Checkbutton(settings_section, variable=self.use_cache)
        use_cache_checkbox.toggle()
        use_cache_checkbox.grid(row=1, column=0)
        use_cache_label = tk.Label(settings_section, text="Use previous cache?\n"
                                                          "Speeds up process if file was parsed before.")
        use_cache_label.grid(row=1, column=1)

        export_ics_checkbox = tk.Checkbutton(settings_section, variable=self.export_as_ics)
        export_ics_checkbox.grid(row=2, column=0)
        export_ics_label = tk.Label(settings_section, text="Export as .ics-file?\n"
                                                           "If unchecked the output type will be csv.")
        export_ics_label.grid(row=2, column=1)

        crash_checkbox = tk.Checkbutton(settings_section)
        crash_checkbox.grid(row=3, column=0)
        crash_label = tk.Label(settings_section, text="Crash randomly?\nThis does not actually do anything.")
        crash_label.grid(row=3, column=1)

        # endregion

        # region parse section
        parse_section = tk.Frame(self.root)
        parse_section.pack(pady=10)

        # parse label
        parse_label = tk.Label(parse_section, text="Parse Timetable(s)", font='Helvetica 10 bold')
        parse_label.pack()

        # parse button
        parse_button = tk.Button(parse_section, text="Parse",
                                 command=lambda: [self.controller.parse_inputs(self.use_cache.get(),
                                                                               self.export_as_ics.get(),
                                                                               self.tos.get())])
        parse_button.pack(pady=5)

        # TOS checkbox
        tos_checkbox = tk.Checkbutton(parse_section, text="Agree to Terms Of Service", variable=self.tos)
        tos_checkbox.pack()

        # endregion

        # region TOS section

        tos_section = tk.Frame(self.root)
        tos_section.pack(pady=10)

        tos_label = tk.Label(tos_section, text="Terms of Service / TOS", font='Helvetica 10 bold')
        tos_label.pack()

        tos_label = tk.Label(tos_section, text="The contents of the TimeTableParser (TTP)\n were compiled with the "
                                               "greatest possible care\n and in accordance with in the best of "
                                               "conscience. \nNevertheless, the provider of this application\n does not"
                                               " assume any liability\nfor the topicality, completeness and"
                                               " correctness\n of the csv/ics files and other content provided.")
        tos_label.pack()

        # endregion
