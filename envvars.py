# Module to store configuration variables for dot-filer

import os


def dotfiles_dir():
    return os.environ["HOME"] + "/Dotfiles"


def register_path():
    return os.environ["HOME"] + "/.local/bin/dotfiles.txt"


# TODO need to change this so that it it prompts for rep url on git initialization
git_repo_remote_url = "git@github.com:AlexHutchison-Dev/Dotfiles.git"
