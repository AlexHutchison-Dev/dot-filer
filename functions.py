import os
import envvars
from shutil import copyfile


def check_for_file(file):
    if os.path.exists(file):
        print("check for file file exists")
        return True
    elif os.path.exists(os.getcwd() + "/" + file):
        return True
    else:
        return False


def add_file(file_path):
    print("Adding file: {}".format(file_path))
    cwd = os.getcwd()
    path_relto_home = path_relative_to_home(file_path)
    print("file_path: %s" % file_path)
    print("path_relto_home: %s" % path_relto_home)
    os.chdir(os.environ["HOME"] + "/.local/bin")
    exists = check_for_file_in_register(
        path_relto_home, "/home/alex/.local/bin/dotfiles.txt"
    )
    print("exists: {}".format(exists))
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
    print("cwd: {}".format(os.getcwd()))
    print("add files to dot files: %s " % path)
    copyfile(path, generate_destination_path(path))


def generate_destination_path(path):
    print(envvars.dotfiles_dir() + path_relative_to_home(path))
    return envvars.dotfiles_dir() + path_relative_to_home(path)


def extract_file_name(path):
    separated = path.split("/")
    return separated[len(separated) - 1]


def extract_target_dir(path):
    dirs = path.split("/")
    del dirs[len(dirs) - 1]
    print("/".join(dirs))
    return "/".join(dirs)


def replace_tilda(path):
    if "~" in path:
        dirs = path.split("/")
        for dir in dirs:
            if "~" in dir:
                dir.replace("~", os.environ["HOME"])
        return "/".join(dirs)
    else:
        return path


def create_directory_structure(path):
    print("creating folder structure!")
    print("path: %s" % path)
    dirs = extract_list_of_directories(path)
    create_dirs(dirs)


def create_dirs(dirs):
    print("creating dirs")
    print("dirs: %s" % dirs)
    print(os.getcwd())
    for index, dir in enumerate(dirs):
        if dir == "":
            print("ERROR: Asked to create directory with blank name")
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
    print("in dirs_created-so_far")
    created = []
    for index, dir in enumerate(dirs):
        created.append(dir)
        if index == target:
            print("created so far: %s" % "/".join(created))
            return "/".join(created)


def extract_list_of_directories(path):
    directories = path.split("/")
    for dir in directories:
        print("extracted dir: %s" % dir)
    del directories[len(directories) - 1]
    del directories[0]
    for dir in directories:
        print("extracted dir: %s" % dir)
    return directories


def copy_file(src, dest):
    size = os.stat(src).st_size
    print(size)
    copyfile(src, dest)
    # TODO complet this


def check_for_dotfiles_directory():
    if not os.path.exists(envvars.dotfiles_dir()):
        os.mkdir(envvars.dotfiles_dir())
    else:
        print("dot-filer directory exists")


def path_relative_to_home(file_path):
    if os.environ["HOME"] in file_path:
        return remove_homedir_path(file_path)
    else:
        return file_path


def remove_homedir_path(path):
    print("remove_homedirs path: %s" % path)
    path = path.replace(os.environ["HOME"], "")
    print("remove_homedirs path: %s" % path)
    return path


def check_for_file_in_register(file_path, register_file):
    print("Checking for file in register: {}".format(file_path))
    found_in_register = False
    if not os.path.exists(register_file):
        return found_in_register
    f = open(register_file, "r+")
    for line in f:
        if file_path == line:
            print("line: {}".format(line))
            found_in_register = True
    return found_in_register
