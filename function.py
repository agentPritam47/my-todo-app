FILEPATH = "todos.txt"


def readfile(filepath=FILEPATH):
    with open(filepath, 'r') as file_read:
        todos_local = file_read.readlines()
        return todos_local


def writefile(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)
