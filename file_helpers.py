import os
import envvars
from shutil import copyfile


def check_for_file(file):
    if os.path.exists(file):
        return True
    elif os.path.exists(os.getcwd() + "/" + file):
        return True
    else:
        return False


def check_for_file_in_register(file_path):
    found_in_register = False
    if not os.path.exists(envvars.register_path()):
        return found_in_register
    else:
        f = open(envvars.register_path(), "r+")
        for line in f:
            if file_path in line:
                found_in_register = True
    return found_in_register


def copy_file(target, destination):
    copyfile(target, destination)


def open_register_for_reading():
    file = open(envvars.register_path(), "r+")
    return file


def read_register_by_line(file):
    lines = file.readlines()
    return lines
