import os
import envvars_class
import file_helpers as fh

env = envvars_class.Env()

def add_file(file_path):
    
    if not fh.path_exists(file_path):
        print("Error: file not found")
    else:
        if not fh.check_for_file_in_register(path_relative_to_home(file_path), env.get_register_path()):
            add_file_to_register(path_relative_to_home(file_path))
            add_file_to_dotfiles_dir(file_path)


def path_relative_to_home(file_path):
    if os.environ["HOME"] in file_path:
        return remove_homedir_path(file_path)
    else:
        return file_path


def remove_homedir_path(path):
    path = path.replace(os.environ["HOME"], "")
    return path


def add_file_to_register(path_relto_home):
    cwd = os.getcwd()

    os.chdir(os.environ["HOME"] + "/.local/bin")

    register = open("dotfiles.txt", "a+")
    register.write("%s\r\n" % (path_relto_home))

    os.chdir(cwd)


def check_for_dotfiles_dir():
    if os.path.exists(env.get_dotfiles_dir()):
        return True
    else:
        os.mkdir(env.get_dotfiles_dir())


def add_file_to_dotfiles_dir(path):
    check_for_dotfiles_dir()
    os.chdir(env.get_dotfiles_dir())
    create_directory_structure(path_relative_to_home(path))
    os.chdir(extract_target_dir(path))
    fh.copy_file(path, generate_destination_path(path))


def create_directory_structure(path):
    dirs = extract_list_of_directories(path)
    create_dirs(dirs)


def extract_target_dir(path):
    dirs = path.split("/")
    del dirs[len(dirs) - 1]
    return "/".join(dirs)


def generate_destination_path(path):
    return env.get_dotfiles_dir() + path_relative_to_home(path)


def extract_list_of_directories(path):
    directories = path.split("/")
    del directories[len(directories) - 1]
    del directories[0]
    return directories


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
    path_parts = [env.get_dotfiles_dir(), dirs_created_so_far(dirs, index)]
    return "/".join(path_parts)


def dirs_created_so_far(dirs, target):
    created = []
    for index, dir in enumerate(dirs):
        created.append(dir)
        if index == target:
            return "/".join(created)
