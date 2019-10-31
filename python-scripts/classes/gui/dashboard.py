import tkinter as tk

from classes.controller.dashboard_controller import DashboardController

# constants
title = "TimeTableParser"
height = 800
width = 600
bgColor = '#263D42'


class Dashboard:
    controller = DashboardController()
    root = tk.Tk()
    background = tk.Canvas(root, height=height, width=width, bg=bgColor, highlightthickness=0)

    def __init__(self):
        self.root.title(title)
        self.center_window_on_screen()

    def show(self):
        self.background.pack()
        self.root.mainloop()

    def center_window_on_screen(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
