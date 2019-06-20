from classes.data_item import DataItem


class DictionaryItem(object):

    """
    Summary
    -------
    Dictionary object for one module type.

    Parameter
    ---------
    event : DataItem    # DataItem object
    """

    module_id: int
    module: str
    pdf_name: str

    def __init__(self, event: DataItem):
        self.module_id = event.module_id
        self.module = event.module
        self.pdf_name = event.pdf_name
