import os
from shutil import copyfile
import filecmp
import envvars_class


env = envvars_class.Env()


def path_exists(file):
    if os.path.exists(file):
        return True
    elif os.path.exists(os.getcwd() + "/" + file):
        return True
    else:
        return False


def check_for_file_in_register(file_path, register):
    found_in_register = False
    if not os.path.exists(register):
        return found_in_register
    else:
        f = open(register, "r+")
        for line in f:
            if file_path in line:
                found_in_register = True
    return found_in_register


def copy_file(target, destination):
    copyfile(target, destination)


def open_register_for_reading(register):
    file = open(register, "r+")
    return file


def read_register_by_line(file):
    lines = file.readlines()
    return lines


def diff_stored_and_current_files(path):
    path = remove_homedir_path(path)
    return filecmp.cmp(env.get_dotfiles_dir() + path, os.environ["HOME"] + path)


def path_relative_to_home(file_path):
    if os.environ["HOME"] in file_path:
        return remove_homedir_path(file_path)
    else:
        return file_path


def remove_homedir_path(path):
    if os.environ["HOME"] in path:
        path.replace(os.environ["HOME"], "")
    return path


def recurse_and_callback_on_file(path, callback):
    return
