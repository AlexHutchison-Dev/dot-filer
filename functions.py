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


def add_file(file_path):
    cwd = os.getcwd()
    path_relto_home = path_relative_to_home(file_path)
    os.chdir(os.environ["HOME"] + "/.local/bin")
    exists = check_for_file_in_register(
        path_relto_home, "/home/alex/.local/bin/dotfiles.txt"
    )
    if not exists:
        register = open("dotfiles.txt", "a+")
        # check for file path in register
        register.write("%s\r\n" % (path_relto_home))
    os.chdir(cwd)
    add_file_to_dotfiles_dir(file_path)


def add_file_to_dotfiles_dir(path):
    os.chdir(envvars.dotfiles_dir())
    create_directory_structure(path_relative_to_home(path))
    os.chdir(extract_target_dir(path))
    copyfile(path, generate_destination_path(path))


def generate_destination_path(path):
    return envvars.dotfiles_dir() + path_relative_to_home(path)


def extract_target_dir(path):
    dirs = path.split("/")
    del dirs[len(dirs) - 1]
    return "/".join(dirs)


def create_directory_structure(path):
    dirs = extract_list_of_directories(path)
    create_dirs(dirs)


def create_dirs(dirs):
    for index, dir in enumerate(dirs):
        if dir == "":
            return
        elif os.path.exists(path_created_so_far(dirs, index)):
            os.chdir(path_created_so_far(dirs, index))

        else:
            os.mkdir(dir)
            os.chdir(path_created_so_far(dirs, index))


def path_created_so_far(dirs, index):
    path_parts = [envvars.dotfiles_dir(), dirs_created_so_far(dirs, index)]
    return "/".join(path_parts)


def dirs_created_so_far(dirs, target):
    created = []
    for index, dir in enumerate(dirs):
        created.append(dir)
        if index == target:
            return "/".join(created)


def extract_list_of_directories(path):
    directories = path.split("/")
    del directories[len(directories) - 1]
    del directories[0]
    return directories


def check_for_dotfiles_directory():
    if not os.path.exists(envvars.dotfiles_dir()):
        os.mkdir(envvars.dotfiles_dir())
    else:
        return


def path_relative_to_home(file_path):
    if os.environ["HOME"] in file_path:
        return remove_homedir_path(file_path)
    else:
        return file_path


def remove_homedir_path(path):
    path = path.replace(os.environ["HOME"], "")
    return path


def check_for_file_in_register(file_path, register_file):
    found_in_register = False
    if not os.path.exists(register_file):
        return found_in_register
    f = open(register_file, "r+")
    for line in f:
        if file_path == line:
            found_in_register = True
    return found_in_register
