import time
import sys
import threading


class ProgressAnimation(object):

    """
    Summary
    -------
    Outsourced parsing animation on second thread.

    Parameter
    ---------
    file_name:  str     # file name
    page_count: int     # pdf page count

    See also
    --------
    Animation starts with constructor call and ends by calling method: thread_progress_animation_end()

        Example:    animation = ProgressAnimation(file_name, page_count)
                    --> Parsing Methods <--
                        animation.set_current_page(page)
                    --> Parsing Methods <--
                    animation.thread_progress_animation_end()
    """

    def __init__(self, file_count: int, current_file: int, file_name: str, page_count: int):
        self.progress_flag = 1
        self.file_count = file_count
        self.current_file = current_file
        self.file_name = file_name
        self.page_count = page_count
        self.current_page = 1
        threading.Thread(target=self.thread_progress_animation_start, args=()).start()

    def thread_progress_animation_start(self):

        animation = [".   ", "..  ", "... "]
        i = 0

        while self.progress_flag:
            sys.stdout.write("\r(file: " + str(self.current_file) + "/" + str(self.file_count) + ") "
                             + "Parsing " + self.file_name + " page " + str(self.current_page)
                             + " of " + str(self.page_count) + " " + animation[i % len(animation)])
            sys.stdout.flush()
            time.sleep(0.3)
            i += 1

    def set_current_page(self, current_page: int):
        self.current_page = current_page

    def thread_progress_animation_end(self):
        self.progress_flag = 0
        print("\r(file: " + str(self.current_file) + "/" + str(self.file_count) + ") "
              + self.file_name + " parsing completed!")
