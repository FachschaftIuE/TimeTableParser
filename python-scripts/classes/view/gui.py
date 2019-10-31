import tkinter as tk

from classes.controller.dashboard_controller import GuiController

# constants
title = "TimeTableParser"
height = 600
width = 300


class Gui:
    controller = GuiController()
    root = tk.Tk()

    def __init__(self):
        self.root.title(title)
        self.center_window_on_screen()

    def show(self):
        self.build_ui()
        self.root.mainloop()

    def center_window_on_screen(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def build_ui(self):
        # region input section

        input_section = tk.Frame(self.root)
        input_section.pack(pady=10)

        input_files = tk.Frame(input_section)
        input_files.pack(side=tk.TOP)

        # label
        input_file_label = tk.Label(input_files, text="TimeTables")
        input_file_label.pack(side=tk.TOP)

        # list of input files
        input_file_list = tk.Listbox(input_files)
        input_file_list.pack(side=tk.LEFT, fill=tk.BOTH)
        input_file_list_scrollbar = tk.Scrollbar(input_files)
        input_file_list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        input_file_list_scrollbar.config(command=input_file_list.yview)
        input_file_list.config(yscrollcommand=input_file_list_scrollbar.set)

        # TODO remove dummy data
        for line in range(100):
            input_file_list.insert(tk.END, "#" + str(line))

        # input buttons
        input_section_buttons = tk.Frame(input_section)
        input_section_buttons.pack(side=tk.BOTTOM)
        clear_button = tk.Button(input_section_buttons, text="Clear")
        clear_button.pack(side=tk.LEFT, padx=10)
        add_button = tk.Button(input_section_buttons, text="Add TimeTable")
        add_button.pack(side=tk.RIGHT, padx=10)

        # endregion

        # region settings section

        settings_section = tk.Frame(self.root)
        settings_section.pack(pady=20)

        # label
        settings_label = tk.Label(settings_section, text="Settings")
        settings_label.grid(row=0, column=0, columnspan=2)

        # checkboxes
        use_cache_checkbox = tk.Checkbutton(settings_section)
        use_cache_checkbox.grid(row=1, column=0)
        use_cache_label = tk.Label(settings_section, text="Use cache from previous parsing if available?")
        use_cache_label.grid(row=1, column=1)

        delete_cache_checkbox = tk.Checkbutton(settings_section)
        delete_cache_checkbox.grid(row=2, column=0)
        delete_cache_label = tk.Label(settings_section, text="Delete cache after parsing?")
        delete_cache_label.grid(row=2, column=1)

        crash_checkbox = tk.Checkbutton(settings_section)
        crash_checkbox.grid(row=3, column=0)
        crash_label = tk.Label(settings_section, text="Crash randomly?")
        crash_label.grid(row=3, column=1)

        # endregion

        # region parse section
        parse_section = tk.Frame(self.root)
        parse_section.pack(pady=10)

        # TODO parse label
        # TODO TOS checkbox

        # parse button
        parse_button = tk.Button(parse_section, text="Parse")
        parse_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # endregion
