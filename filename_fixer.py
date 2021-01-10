def remove_invalid_chars(file_name):
    not_allowed = ['*', '"', '/', '\\', ':', ';', '|', '?', '<', '>']
    for char in not_allowed:
        if char in file_name:
            file_name = file_name.replace(char, '_')
    
    return file_name