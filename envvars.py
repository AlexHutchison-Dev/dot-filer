# Module to store configuration variables for dot-filer

import os


def register_path():
    return os.environ["HOME"] + "/" + "register.txt"


def dotfiles_dir():
    return os.environ["HOME"] + "/dotfiles"
