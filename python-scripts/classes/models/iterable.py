from abc import ABC
from ..box import Box


class BoxContent:
    data_box = None
    content = None

    def __init__(self, data_box, content):
        self.data_box = data_box
        self.content = content

class Iterable(ABC):
    main_box = None
    min_box = Box([0,0,0,0])
    content = ""
    content_box = Box([0,0,0,0])

    def __init__(self, main_box):
        self.main_box = main_box

    def get_information(self, box):
        raise NotImplementedError


class ModuleNameFinder(Iterable):
    def __init__(self, main_box):
        Iterable.__init__(self, main_box)

    def get_information(self, box_content: BoxContent):

        module_name_box = list()

        # Check if centre of main_box and module_description_box match than we know it is the module name -> centred
        if abs(self.main_box.x_centre() - box_content.data_box.x_centre()) < 1:
            if (box_content.data_box.x_centre() < self.min_box.x_centre()) and (box_content.data_box.y_centre() < self.content_box.y_centre()):

                # Set the smallest box to the current box, is later used to find the left lower box
                self.min_box = box_content.data_box
            module_name_box.append(box_content.data_box)

            # Set main_box to current box. Is later used to know where left and right is
            self.main_box = box_content.data_box

            # Add the name of the module to content. Is used for multiline module names
            self.content += box_content.content + " "
            self.content_box = module_name_box[0]

class ModuleProfFinder(Iterable):
    module_name_box = None

    def __init__(self, main_box):
        Iterable.__init__(self, main_box)

    def get_information(self, box_content: BoxContent):

        # Check if current box is right of the main box and higher than the module name box
        if (self.main_box.x_centre() < box_content.data_box.x_centre()) and (
                self.module_name_box.y_centre() < box_content.data_box.y_centre()):
            self.content += box_content.content + " "


class ModuleRoomFinder(Iterable):
    module_name_box = None

    def __init__(self, main_box):
        Iterable.__init__(self, main_box)

    def get_information(self, box_content: BoxContent):

        # Check if the current lower than the module name box and right to the smallest left box
        if (self.min_box.x_centre() < box_content.data_box.x_centre()) and (
                self.module_name_box.y_centre() > box_content.data_box.y_centre()):
            self.content += box_content.content + " "

