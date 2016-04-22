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


class CompleteSearch(Thread):
    """
    | This class is Thread class children.The return_equals stores all files and directories those are in
    | or into the included directories of that with name equals word string. or returns the result
    """
    def __init__(self, directory, word):
        super(CompleteSearch, self).__init__()
        self.directory = directory
        self.word = word
        self.is_pattern=False
        if self.word[0] == '[' and self.word[-1] == ']':
            self.is_pattern= True

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
            element = element.lower()
            word = word.lower()
            word_index = element.find(word)
            if not element:
                continue

            elif self.is_pattern :
                print "Starting Pattern Search"
                if self.search_s(element) :
                    result.append(directory + "\\" + element)

                elif element.split('.')[-1] == "txt":
                    print element.split('.')[-1]
                    try:
                        text_file = open(self.directory + "\\" + element, 'r')
                        line = text_file.readline()
                        while line:
                            if search_s(line):
                                result.append([self.directory + "\\" + element, ])
                                break
                            line = text_file.readline()
                        text_file.close()
                    except IOError:
                        print 'kir'
                        print

            elif element == self.word:
                result.append(directory + "\\" + element)
            elif word_index + 1:
                # print directory + "\\" + element
                result.append([self.directory + "\\" + element, word_index, word_index + len(word)])
            elif element.split('.')[-1] == "txt":
                print element.split('.')[-1]
                try:
                    text_file = open(self.directory + "\\" + element, 'r')
                    line = text_file.readline()
                    while line:
                        if word in line:
                            result.append([self.directory + "\\" + element, word_index, word_index + len(word)])
                            break
                        line = text_file.readline()
                    text_file.close()
                except IOError:
                    print 'kir'
                    print
            elif isdir(directory + "\\" + element):
                thread_obj = CompleteSearch(directory + "\\" + element, self.word)
                threads_list.append(thread_obj)
                thread_obj.start()
                thread_obj.join()

    def run(self):
        self.return_equals(self.directory, self.word)

    def search_s(self, word2):

        order_word = self.word[1:len(self.word)-1].split()

        pointer = 0

        if order_word[0][0] == "^":
            if word2[pointer:pointer+len(order_word[0])-1] == order_word[0][1:] :
                return True
        else:
            for opp in order_word:
                if len(opp) == 3 and opp[1] == "-":
                    if (ord(word2[pointer]) > ord(opp[0])) and (ord(word2[pointer]) < ord(opp[2])):
                        pointer += 1
                    else :
                        return False
                elif opp[0] == "?" :
                    if word2[pointer:pointer+len(opp)-1] == opp[1:] :
                        return False
                    else :
                        pointer += len(opp) - 1
                elif opp[0] == "*" :
                    pointer += 1

                else:
                    if word2[pointer:pointer+len(opp)] == opp :
                        pointer += len(opp)
                    else :
                        return False
        return True




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
    if current_directory:
        searcher_object = CompleteSearch(current_directory, word)
        searcher_object.start()
        searcher_object.join()
        return remove_equals(search_result_list)

    else:
        for cleaner in range(len(search_result_list)):
            search_result_list.pop()
        for driver in drivers():
            searcher_object = CompleteSearch(driver, word)
            searcher_object.start()
        return remove_equals(search_result_list)


def search_s(word, current_directory):
    if word[0] == '[' and word[-1] == ']':
        order_word = word[1:len(word)-1].split()
        if current_directory:
            try:
                files = listdir(current_directory)
            except WindowsError:
                return
            for element in files:
                pointer = 0
                is_word=True
                if order_word[0][0] == "^":
                    if element[pointer:pointer+len(order_word[0])-1] == order_word[0][1:] :
                        return True
                else:
                    for opp in order_word:
                        if len(opp) == 3 and opp[1] == "-":
                            if (ord(element[pointer]) > ord(opp[0])) and (ord(element[pointer]) < ord(opp[2])):
                                pointer += 1
                            else :
                                is_word = False
                                break
                        elif opp[0] == "?" :
                            if element[pointer:pointer+len(opp)-1] == opp[1:] :
                                is_word = False
                                break
                            else :
                                pointer += len(opp) - 1
                        elif opp[0] == "*" :
                            pointer += 1

                        else:
                            if element[pointer:pointer+len(opp)] == opp :
                                pointer += len(opp)
                            else :
                                is_word = False
                                break
                if is_word :
                    return True

