import ntpath


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class GuiController:

    def __init__(self):
        self.inputs = []

    def clear_inputs(self):
        self.inputs.clear()

    def parse_inputs(self, use_cache, export_as_ics, tos):
        print(use_cache)
        print(export_as_ics)
        print(tos)

