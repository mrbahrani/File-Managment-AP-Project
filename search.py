def search(word, current_directory):
    file_type = ""
    if len(word.split(".") > 1):
        file_type = word.split(".")[-1]