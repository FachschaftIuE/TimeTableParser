import ntpath


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class GuiController:

    def __init__(self):
        self.inputs = []

    def clear_inputs(self):
        self.inputs.clear()
