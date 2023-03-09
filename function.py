FILEPATH = "todos.txt"


def readfile(filepath=FILEPATH):
    with open(filepath, 'r') as file_read:
        todos_locall = file_read.readlines()
        return todos_locall


def writefile(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)
