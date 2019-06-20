from helper.data_output import create_csv, create_ics
from classes.data_item import DataItem
from classes.dictionary_item import DictionaryItem
from typing import List
import datetime
from termcolor import *


def show_application_disclaimer():

    """
    Summary
    -------
    This function outputs the limitation of liability (Disclaimer).
    """
    print(colored("                                         FH-Kiel, Time Table Parser                                         ", attrs=['reverse']))
    print(colored("############################################################################################################", 'magenta'))
    print(colored("Limitation of liability (Disclaimer):\n", 'magenta'))
    print(colored("The contents of the TimeTableParser (TTP) were compiled with the greatest possible care and in accordance", 'magenta'))
    print(colored("with in the best of conscience. Nevertheless, the provider of this application does not assume any liability", 'magenta'))
    print(colored("for the topicality, completeness and correctness of the ical/ics files and other content provided.", 'magenta'))
    print(colored("############################################################################################################\n", 'magenta'))


def user_select(data: List[DictionaryItem]):

    """
    Summary
    -------
    This function creates an interface to create an individual list of modules. Which has to
    be filtered.

    Parameter
    ---------
    data : list     # DictionaryItem-list

    Returns
    -------

    data : list     # FinalList with Integers which have to be in the final calender.
    """
    
    pdfelements = list()
    pdfelements.append(data[0].pdf_name)
    text_seletion_type = "Whitelist ('" + colored("W", 'green') + "') / Blacklist ('" + colored("B", 'green') + "') / All ('" + colored(
        "A", 'green') + "')"
    finallist = list()
    templist = list()

    for event in data:
        flag = 1
        for element in pdfelements:
            if event.pdf_name == element:
                flag = 0
        if flag:
            pdfelements.append(event.pdf_name)

    for element in pdfelements:
        carrierlist = list()

        print("\nCurrently selected PDF-file: ", colored(element, attrs=['bold']))
        print("\nID\tModule")
        for event in data:
            if event.pdf_name == element:
                carrierlist.append(event)
                print(colored(str(event.module_id), 'yellow', attrs=['bold']) + "\t" + event.module)
        print("\n" + colored("What kind of selection do you want?", attrs=['reverse']))
        print(text_seletion_type)
        print("For help press ('" + colored("?", 'green') + "')")

        correct_input = 1
        while correct_input:
            user_input = input()
            if user_input == 'W' or user_input == 'w':
                correct_input = 0
                templist = whitelist(carrierlist)

            elif user_input == 'B' or user_input == 'b':
                correct_input = 0
                templist = blacklist(carrierlist)

            elif user_input == 'A' or user_input == 'a':
                correct_input = 0
                templist = add_all(carrierlist)

            elif user_input == '?':
                print(colored("\n-Whitelist-", 'yellow', attrs=['bold']) + ": Choose this if you want to add just a few modules.\n"
                      "Selected modules will be added to your calendar\n" +
                      colored("-Blacklist-", 'yellow', attrs=['bold']) + ": Choose this if you want to unselect some modules.\n"
                      "All modules which you had chosen, will not be in your calendar.\n" +
                      colored("-All-", 'yellow', attrs=['bold']) + ": All of the displayed modules will be added to your calendar.")

            else:
                print(colored('Incorrect input!', 'red'))

        finallist = finallist + templist
    if len(finallist) == 0:
        print(colored("You have no modules selected!", 'red'))
        return finallist
    print("\nYour selected modules:")
    for event in data:
        for index in finallist:
            if event.module_id == index:
                print(str(event.module_id) + "\t" + event.module)

    return finallist


def blacklist(carrier: List[DictionaryItem]):

    """
    Summary
    -------
    This function creates a whitelist of modules using a blacklist.

    Parameter
    ---------
    data : list     # Part of the DictionaryItem-list

    Returns
    -------

    data : list     # Returns index of data which has to be in the final list
    """

    whitelist = list()
    blacklist = list()

    print("\n" + colored("Which module would you like to remove?", attrs=['reverse']))
    print("Please select module " + colored("ID", 'yellow', attrs=['bold']) + " which you want to ignore.")
    print("To finish process press ('" + colored("D", 'green') + "')")

    while True:
        user_input = input()
        err = 1
        try:
            if user_input == "D" or user_input == "d":
                break

            for item in carrier:
                if item.module_id == int(user_input):
                    blacklist.append(int(user_input))
                    err = 0
                    break
            if err:
                print(colored("Could not find module.", 'red'))
        except:
            print(colored("Incorrect input!", 'red'))

    for item in carrier:
        flag = 1
        for index in blacklist:
            if item.module_id == index:
                flag = 0
                break

        if flag:
            whitelist.append(item.module_id)

    return whitelist


def whitelist(carrier: List[DictionaryItem]):

    """
    Summary
    -------
    This function creates a whitelist of modules.

    Parameter
    ---------
    data : list     # Part of the DictionaryItem-list

    Returns
    -------

    data : list     # Returns index of data which has to be in the final list
    """

    whitelist = list()

    print("\n" + colored("Which module would you like to add?", attrs=['reverse']))
    print("Please select module " + colored("ID", 'yellow', attrs=['bold']) + " to add")
    print("To finish process press ('" + colored("D", 'green') + "')")

    while True:
        user_input = input()
        flag = 0
        err = 1

        try:
            if user_input == "D" or user_input == "d":
                break


            for item in carrier:
                if item.module_id == int(user_input):
                    flag = 1
                    err = 0
                    break
            if err:
                print(colored("Could not find module.", 'red'))
            if flag:
                whitelist.append(int(user_input))
        except:
            print(colored("Incorrect input!.", 'red'))

    return whitelist


def add_all(carrier: List[DictionaryItem]):

    """
    Summary
    -------
    This function creates a whitelist of modules using a blacklist. But adds all modules

    Parameter
    ---------
    data : list     # Part of the DictionaryItem-list

    Returns
    -------

    data : list     # Returns index of data which has to be in the final list
    """

    whitelist = list()
    blacklist = list()

    for item in carrier:
        flag = 1
        for index in blacklist:
            if item.module_id == index:
                flag = 0
                break

        if flag:
            whitelist.append(item.module_id)

    return whitelist


def format_select(data: List[DataItem]):

    """
    Summary
    -------
    This function asks for preferd file format.
    """

    print("\n" + colored("Which output format do you want?", attrs=['reverse']))
    print(".csv = Google calendar")
    print(".ics = MacOS/iOS calendar")
    print(".csv ('" + colored("C", 'green') + "') / .ics ('" + colored("I", 'green') + "')")

    correct_input = 1
    while correct_input:
        question_input = input()

        if question_input == 'C' or question_input == 'c':
            correct_input = 0
            create_csv(data, name_select())
            print(colored("\nCalendar created, program shutdown!\n", 'magenta'))
            print(colored("You can find your new calendar in your output folder ('/data/output').\n", 'magenta'))

        elif question_input == 'I' or question_input == 'i':
            correct_input = 0
            create_ics(data, name_select())
            print(colored("\nCalendar created, program shutdown!\n", 'magenta'))
            print(colored("You can find your new calendar in your output folder ('/data/output').\n", 'magenta'))

        else:
            print(colored("Incorrect input!", 'red'))


def name_select():

    """
    Summary
    -------
    This function asks for a prefered filename.

    Returns
    -------
    name : str    # User prefered filename or default filename with timestamp
    """

    print("\n" + colored("Do you want to change the default filename?", attrs=['reverse']))
    print("Yes ('" + colored("Y", 'green') + "') / No ('" + colored("N", 'green') + "')")

    correct_input = 1
    while correct_input:
        question_input = input()

        if question_input == 'Y' or question_input == 'y':
            correct_input = 0
            print(colored("Enter filename:", attrs=['reverse']))
            return input()

        elif question_input == 'N' or question_input == 'n':
            correct_input = 0
            return "calendar_" + datetime.datetime.utcnow().strftime('%d%m%Y%H%M%S')

        else:
            print(colored("Incorrect input!", 'red'))


