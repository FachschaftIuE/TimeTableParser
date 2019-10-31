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
        # background
        tk.Canvas(self.root, height=height, width=width, highlightthickness=0).pack()

        # input section
        input_section = tk.Frame(self.root)
        input_section.place(relwidth=1, relheight=0.4)

        input_files = tk.Frame(input_section)
        input_files.pack(side=tk.TOP, pady=10)

        input_file_label = tk.Label(input_files, text="TimeTables")
        input_file_label.pack(side=tk.TOP)

        input_file_list = tk.Listbox(input_files)
        input_file_list.pack(side=tk.LEFT, fill=tk.BOTH)
        input_file_list_scrollbar = tk.Scrollbar(input_files)
        input_file_list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        input_file_list_scrollbar.config(command=input_file_list.yview)
        input_file_list.config(yscrollcommand=input_file_list_scrollbar.set)

        for line in range(100):
            input_file_list.insert(tk.END, "#" + str(line))

        input_section_buttons = tk.Frame(input_section)
        input_section_buttons.pack(side=tk.BOTTOM)
        clear_button = tk.Button(input_section_buttons, text="Clear")
        clear_button.pack(side=tk.LEFT, padx=10)
        add_button = tk.Button(input_section_buttons, text="Add TimeTable")
        add_button.pack(side=tk.RIGHT, padx=10)

        # settings section
        settings_section = tk.Frame(self.root, bg="white")
        settings_section.place(rely=0.4, relwidth=1, relheight=0.4)

        # parse section
        parse_section = tk.Frame(self.root, bg="red")
        parse_section.place(rely=0.8, relwidth=1, relheight=0.2)
        parse_button = tk.Button(parse_section, text="Parse")
        parse_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
