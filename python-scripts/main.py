from classes.view.gui import Gui


def main():
    # region new main

    Gui().show()

    # endregion

    # # region old main TODO remove
    #
    # colorama.init()
    # show_application_disclaimer()
    #
    # data = list()
    #
    # files = file_handler(read_input_folder(), read_cache_folder())
    #
    # # security question!
    # if files is not None:
    #     if files["files_to_parse"].__len__() == 0 and files["files_to_load"].__len__() == 0:
    #         print(f'\n {colored("No file selected, program shutdown!", "red")}')
    #         return
    #
    #     if files["files_to_parse"].__len__() > 0:
    #         print('Start Parsing (This will take a moment, grab a coffee!)')
    #
    #     for file_index in range(files["files_to_parse"].__len__()):
    #         page_count = get_pdf_pages(files["files_to_parse"][file_index]["file_path"])
    #         animation = ProgressAnimation(files["files_to_parse"].__len__(), file_index + 1,
    #                                       files["files_to_parse"][file_index]["file_name"], page_count)
    #
    #         for page in range(page_count):
    #
    #             animation.set_current_page(page + 1)
    #
    #             file_container = Loader(files["files_to_parse"][file_index]["file_path"],
    #                                     files["files_to_parse"][file_index]["file_name"], page)
    #
    #             timetable = Timetable()
    #
    #             t_controller = TimetableController(file_container, timetable)
    #             t_controller.create_timetable_information()
    #             t_controller.send_data_to_timetable()
    #
    #             timetable.search_modules()
    #             timetable.get_weeks()
    #             timetable.find_modules(data)
    #
    #         create_json_from_data_item(data, files["files_to_parse"][file_index]["file_name"])
    #         animation.thread_progress_animation_end()
    #     print("")  # Empty line after parsing
    #
    #     for file_index in range(files["files_to_load"].__len__()):
    #         data_item_from_json(data, files["files_to_load"][file_index]["file_path"])
    #
    #     filter_data_list(data, user_select(create_data_dictionary(data)))
    #
    #     format_select(data)
    #
    # # endregion


if __name__ == "__main__":
    main()
