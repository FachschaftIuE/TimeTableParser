import ntpath
import os.path
import pathlib
import time
from datetime import datetime
from time import mktime
from typing import List

from termcolor import *

input_folder = pathlib.Path.cwd().joinpath('data', 'input')
cache_folder = pathlib.Path.cwd().joinpath('data', 'cache')


def get_cached_file_for(filename):
    return pathlib.Path().joinpath(cache_folder, filename.replace('.pdf', '.json'))

def convert_files(input_files, file_type):
    files = list()

    for file in input_files:
        file_name = path_leaf(file).replace(file_type, "")
        # temp_file = temp_file.replace(input_folder + "/", "")   # Replace for MAC path
        # temp_file = temp_file.replace(input_folder + "\\", "")  # Replace for Windows path

        temp_dict = {"file_name": file_name, "file_path": file, "file_edit": None}
        temp_dict["file_edit"] = \
            datetime.fromtimestamp(mktime(time.localtime(os.path.getmtime(temp_dict["file_path"]))))

        files.append(temp_dict)

    return files


def read_input_folder():
    return convert_files(input_folder.rglob('*.pdf'), '.pdf')


def read_cache_folder():
    return convert_files(cache_folder.rglob('*.json'), '.json')


def file_handler(input_files: List[dict], cache_files: List[dict], use_cache):

    files_to_parse = list()
    files_to_load = list()

    if cache_files.__len__() > 0:
        for input_file in input_files:
            for save_file in cache_files:
                if input_file["file_name"] == save_file["file_name"]:
                    if use_cache:
                        files_to_load.append(save_file)
                    else:
                        files_to_parse.append(input_file)

    else:
        for file in input_files:
            files_to_parse.append(file)

    temp_dict = {"files_to_parse": files_to_parse, "files_to_load": files_to_load}
    return temp_dict


def path_leaf(file_path):
    head, tail = ntpath.split(file_path)
    return tail or ntpath.basename(head)
