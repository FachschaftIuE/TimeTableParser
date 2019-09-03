import glob
from typing import List
from termcolor import *
import os.path
import time
from time import mktime
from datetime import datetime
import pathlib

input_folder = pathlib.Path.cwd().joinpath('data', 'input')
cache_folder = pathlib.Path.cwd().joinpath('data', 'cache')


def read_input_folder():
    input_files = input_folder.rglob('*.pdf')
    # input_files = glob.glob(input_folder + "/*.pdf")

    files = list()

    for file in input_files:
        temp_file = file.name.replace(".pdf", "")
        # temp_file = temp_file.replace(input_folder + "/", "")   # Replace for MAC path
        # temp_file = temp_file.replace(input_folder + "\\", "")  # Replace for Windows path

        temp_dict = {"file_name": temp_file, "file_path": file, "file_edit": None}
        temp_dict["file_edit"] = datetime.fromtimestamp(mktime(time.localtime(os.path.getmtime(temp_dict["file_path"]))))

        files.append(temp_dict)

    return files


def read_cache_folder():
    cache_files = cache_folder.rglob('*.json')
    # cache_files = glob.glob(cache_folder + "/*.json")

    files = list()

    for file in cache_files:
        temp_file = file.name.replace(".json", "")
        # temp_file = temp_file.replace(cache_folder + "/", "")   # Replace for MAC path
        # temp_file = temp_file.replace(cache_folder + "\\", "")  # Replace for Windows path

        temp_dict = {"file_name": temp_file, "file_path": file, "file_edit": None}
        temp_dict["file_edit"] = datetime.fromtimestamp(mktime(time.localtime(os.path.getmtime(temp_dict["file_path"]))))

        files.append(temp_dict)

    return files


def file_handler(input_files: List[dict], cache_files: List[dict]):

    if input_files.__len__() > 0:

        print("Files in input-folder:")
        print("\nID\tPDF")

        for index in range(input_files.__len__()):
            print(f"{colored((index + 1).__str__(), 'yellow', attrs=['bold'])} \t {input_files[index]['file_name']}")

        print("\n" + colored("Which files do you want to parse?", attrs=['reverse']))
        print("Please select file " + colored("ID", 'yellow', attrs=['bold']) + " to add")
        print("To finish process press ('" + colored("D", 'green') + "')")

        temp_input_files = list()

        while True:
            user_input = input()
            err = 1

            try:
                if user_input == "D" or user_input == "d":
                    break

                for index in range(input_files.__len__()):
                    if index == (int(user_input) - 1):
                        if input_files[index] not in temp_input_files:
                            temp_input_files.append(input_files[index])
                            err = 0
                            break
                        else:
                            print(colored("File already in list.", 'red'))
                            err = 0
                            break
                if err:
                    print(colored("Could not find file.", 'red'))
            except:
                print(colored("Could not find file.", 'red'))

        files_to_parse = list()
        files_to_load = list()

        if cache_files.__len__() > 0:
            for input_file in temp_input_files:
                file_added = 0
                for save_file in cache_files:
                    if input_file["file_name"] == save_file["file_name"]:

                        edit_time = save_file["file_edit"].strftime("%d.%m.%Y - %H:%M")

                        print("\n" + colored("Should the file " + colored("(" + input_file["file_name"] + ")", 'white', attrs=['bold', 'reverse']), attrs=['reverse'])
                              + colored(" (parsed on: " + edit_time + ") be parsed again?", attrs=['reverse']))
                        print("Yes ('" + colored("Y", 'green') + "') or No ('" + colored("N", 'green') + "')")

                        correct_input = 1
                        while correct_input:
                            question_input = input()

                            if question_input == 'Y' or question_input == 'y':
                                correct_input = 0
                                files_to_parse.append(input_file)
                                file_added = 1

                            elif question_input == 'N' or question_input == 'n':
                                correct_input = 0
                                files_to_load.append(save_file)
                                file_added = 1
                            else:
                                print(colored("Incorrect input!", 'red'))

                if file_added == 0:
                    files_to_parse.append(input_file)

        else:
            for file in temp_input_files:
                files_to_parse.append(file)

        temp_dict = {"files_to_parse": files_to_parse, "files_to_load": files_to_load}
        return temp_dict

    else:
        if cache_files.__len__() > 0:

            print("No files in input-folder!")
            print("\nFiles in cache-folder:")
            print("\nID\tPDF")

            for index in range(cache_files.__len__()):
                print((index + 1).__str__() + "\t" + cache_files[index]["file_name"])

            print("\nWhich files do you want to load?")
            print("To finish process press 'D'")

            temp_load_files = list()

            while True:
                user_input = input()
                err = 1

                try:
                    if user_input == "D" or user_input == "d":
                        break

                    for index in range(cache_files.__len__()):
                        if index == (int(user_input) - 1):
                            if cache_files[index] not in temp_load_files:
                                temp_load_files.append(cache_files[index])
                                err = 0
                                break
                            else:
                                print("File already in list.")
                                err = 0
                                break
                    if err:
                        print("Could not find file.")
                except:
                    print("Could not find file.")

            files_to_parse = list()
            files_to_load = list()

            for file in temp_load_files:
                files_to_load.append(file)

            temp_dict = {"files_to_parse": files_to_parse, "files_to_load": files_to_load}
            return temp_dict

        else:
            print("No files found!")
