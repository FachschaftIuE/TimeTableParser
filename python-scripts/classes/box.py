class Box:
    """
    Container for coordinates
    """
    x0 = 0
    x1 = 0
    y0 = 0
    y1 = 0

    def __init__(self, array: list):
        self.x0 = array[0]
        self.x1 = array[2]
        self.y0 = array[1]
        self.y1 = array[3]

    def x_centre(self):
        """
        Return centre in x directions
        """
        return round(self.x0 + ((self.x1 - self.x0) / 2), 3)

    def y_centre(self):
        """
        Return centre in y directions
        """
        return round(self.y0 + ((self.y1 - self.y0) / 2), 3)