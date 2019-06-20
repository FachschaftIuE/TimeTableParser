import pdfquery


class Loader:
    """
    This class was designed to load and contain file-information from a pdf-file.
    """

    def __init__(self, path_to_file, file_name, page_number=None):
        """
        Constructor of FileContainer Class, sets file_path and all the existing time stamps

        Parameters
        ----------
        path_to_file: str
            path where to read file from
        """
        self.__file = None
        self.__file_path = path_to_file
        self.__file_name = file_name
        self.__load_file(page_number)
        self.__pages = list()

    def __load_file(self, page_number):
        """
        Method checks which page to load, if page_number is not specified, the whole document will be loaded.
        Parameters
        ----------
        page_number: int
            page number to load
        """
        self.__file = pdfquery.PDFQuery(self.__file_path)
        if page_number is None:
            self.__file.load()
        else:
            self.__file.load(page_number)

    def get_page(self, page_number):
        """
        Returns a specified page from loaded file

        Parameters
        ----------
        page_number: int
            page to return

        Returns
        -------
        page:
        """
        return self.__file.get_page(page_number)

    def get_file(self):
        return self.__file

    def get_file_name(self):
        return self.__file_name
