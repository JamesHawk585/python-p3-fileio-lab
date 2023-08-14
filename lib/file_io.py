def write_file(file_name, file_content):
    with open(file_name + '.txt', mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)

def append_file(file_name, append_content):
    pass

def read_file(file_name):
    pass
