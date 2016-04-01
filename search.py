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
search_list = []                                        # This list contains search results


def return_equals(directory, word, result=search_list):
    """
    | This void function saves all including files and directories with same name with word to the search_list list.
    return_equals(directory, word[, result=search_list])
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
    # print directories
    for element in directories:
        if not element:
            continue
        elif element == word:
            result.append(directory + "\\" + element)
        elif isdir(directory + "\\" + element):
            return_equals(directory + "\\" + element + "\\", word)


def return_equals_step_by_step(directory, word, result=search_list):
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
    directories = listdir(directory)
    if "$Recycle.Bin" in directories:
        directories.remove("$Recycle.Bin")
    if "*" in directories:
        directories.remove("*")
    for element in directories:
        index_start = element.find(word)
        if not element:
            continue
        elif index_start != -1:
            result.append([directory + "\\" + element, index_start, index_start + len(word)])
        elif isdir(directory + " \\" + element):
            return_equals((directory + "\\" + element).replace("\\", "\\\\"), word)


def search(word, current_directory, search_result_list=search_list):
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
                results.append((current_directory + "\\" + element))
        if results:
            return results
        else:
            # return "No matching item found"
            return []
    else:
        for cleaner in range(len(search_result_list)):
            search_result_list.pop()
        for driver in drivers():
            return_equals(driver, word)
        return search_list


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
        files = listdir(current_directory)
        for element in files:
            index_start = element.find(word)
            if index_start != -1:
                results.append([current_directory + element, index_start, index_start + len(word)])
        if results:
            return results
    else:
        for cleaner in range(len(search_result_list)):
            search_result_list.pop()
        for driver in drivers():
            return_equals_step_by_step(driver, word)
        return search_list
