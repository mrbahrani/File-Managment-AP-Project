"""
| This file including all functions and variables needed for searching inside directories of all of the memory.
| The list of including functions:
| 1.return_equals
| 2.return_equals_step_by_step
| 3.search
| 4.step_by_step_search
|
| Including variables:
| 1.search_list:list
"""

from os import listdir
from funcs import drivers
from os.path import isdir
from funcs import remove_equals
from threading import Thread
from string import uppercase, lowercase
search_list = []                                        # This list contains search results
threads_list = []


class StepSearch(Thread):
    def __init__(self, directory, word):
        super(StepSearch, self).__init__()
        self.directory = directory
        self.word = word

    def return_equals_step_by_step(self, directory, word, result=search_list):
        """
        | This void function saves all including files and directories with same name with word to the search_list list
        | With below pattern:
        | [directory or file path, start of index of matched case in file or directory name,end of index of matched case in
        | file or directory name].
        return_equals_step_by_step(directory, word[, result=search_list])
        :rtype: object
        :param directory:str
        :param word:str
        :param result:list

        """
        try:
            directories = listdir(directory)
        except WindowsError:
            directories = []
        if "$Recycle.Bin" in directories:
            directories.remove("$Recycle.Bin")
        if "*\\*" in directories:
            directories.remove("*\\*")
        for element in directories:
            element = element.lower()
            word_index = element.find(word)
            if not element:
                continue
            elif word_index + 1:
                print directory + "\\" + element
                result.append([directory + "\\" + element, word_index, word_index + len(word)])
            elif isdir(directory + "\\" + element):
                print "Again"
                print directory + "\\" + element
                thread_obj = StepSearch(directory + "\\" + element + "\\", word)
                threads_list.append(thread_obj)
                thread_obj.start()
                thread_obj.join()

    def run(self):
        self.return_equals_step_by_step(self.directory, self.word)


class CompleteSearch(Thread):
    def __init__(self, directory, word):
        super(CompleteSearch, self).__init__()
        self.directory = directory
        self.word = word

    def return_equals(self, directory, word, result=search_list):
        """
        | This void function saves all including files and directories with same name with word to the search_list list.
        return_equals(directory, word[, result=search_list])
        :rtype: object
        :param directory:str
        :param word:str
        :param result:list

        """
        try:
            directories = listdir(self.directory)
        except WindowsError:
            directories = []
        if "$Recycle.Bin" in directories:
            directories.remove("$Recycle.Bin")
        if "*\\*" in directories:
            directories.remove("*\\*")
        # print directories
        for element in directories:
            if not element:
                continue
            elif element == self.word:
                result.append(directory + "\\" + element)
            elif isdir(directory + "\\" + element):
                thread_obj = CompleteSearch(directory + "\\" + element, self.word)
                threads_list.append(thread_obj)
                thread_obj.start()
                thread_obj.join()

    def run(self):
        self.return_equals(self.directory, self.word)


def complete_search(word, current_directory, search_result_list=search_list):
    """
    | This function returns search results of files and directories with same name of word.
    | First current directory searches and if there is any result, will return as a list
    | If user searches in home page, all drivers searches for results and the result will return as a list;
    search(word, current_directory[, search_result_list=search_list])
    :param word:str
    :param current_directory:str
    :param search_result_list:list
    :return list
    """
    results = []
    if current_directory:
        files = listdir(current_directory)
        for element in files:
            if element == word:
                search_result_list.append(current_directory + "\\" + element)
        else:
            # return "No matching item found"
            for element in files:
                searcher_object = CompleteSearch(current_directory + element, word)
                searcher_object.start()
        return remove_equals(search_result_list)

    else:
        for cleaner in range(len(search_result_list)):
            search_result_list.pop()
        for driver in drivers():
            searcher_object = CompleteSearch(driver, word)
            searcher_object.start()
        return remove_equals(search_result_list)


def step_by_step_search(word, current_directory, search_result_list=search_list):
    """
    | | This function returns search results of files and directories with same name of word.
    | First current directory searches and if there is any result, will return as a list
    | If user searches in home page, all drivers searches for results and the result will return as a list in below
    | pattern:
    | [directory or file path, start of index of matched case in file or directory name,end of index of matched case in
    | file or directory name].
    |
    step_by_step_search(word, current_directory[, search_result_list=search_list]):
    :param word:str
    :param current_directory:str
    :param search_result_list:list
    :return list
    """
    results = []
    if current_directory:
        try:
            files = listdir(current_directory)
        except WindowsError:
            return
        for element in files:
            word_index = element.find(word)
            if word_index + 1:
                print current_directory + "\\" + element
                search_result_list.append([current_directory + "\\" + element, word_index, word_index + len(word)])

            else:
                # return "No matching item found"
                searcher_obj = StepSearch(current_directory, word)
                searcher_obj.start()
                searcher_obj.join()
        return remove_equals(search_result_list)
    else:
        for cleaner in range(len(search_result_list)):
            search_result_list.pop()

        for driver in drivers():
            searcher_obj = StepSearch(driver, word)
            searcher_obj.start()
        return remove_equals(search_result_list)


def search(word, current_directory):
    if word[0] == '[' and word[-1] == ']':
        