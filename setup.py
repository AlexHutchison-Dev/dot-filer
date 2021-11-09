import os
import envvars


def startup_checks():
    check_register_file_exists()
    check_dotfiles_dir_exists()


def check_register_file_exists():
    if os.path.exists(envvars.register_path()):
        return
    else:
        create_dotfiles_register()


def check_dotfiles_dir_exists():
    if os.path.exists(envvars.dotfiles_dir()):
        return
    else:
        create_dotfiles_dir()


def create_dotfiles_register():
    cwd = os.getcwd()
    os.chdir(os.environ["HOME"] + "/.local/bin/")
    f = open("dotfiles.txt", "x")
    f.close()
    os.chdir(cwd)


def create_dotfiles_dir():
    os.mkdir(envvars.dotfiles_dir())
