from ..box import Box

class EventMeta:
    """
    Helper class to display information about day in a certain way
    """

    def __init__(self, day_name, x0, x1):

        self.day_name = day_name
        self.x0 = x0
        self.x1 = x1
        self.width = round(x1-x0, 2)

    def print(self):

        return "Tag: " + self.day_name + " X0: " + str(self.x0) + " X1: " + str(self.x1) + " Width: " + str(self.width)

    def get_box(self):
        return Box([self.x0, 0, self.x1, 0])
