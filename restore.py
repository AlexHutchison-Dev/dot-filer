# this module is to go through all the files stored in the dotfiles directory and insert them into
# the file system in the correct inplace with the users home directory in place of the Dotfiles
# directory

import os
import envvars_class
import recursor as r

env = envvars_class.Env()


def restore():
    print("restore called")
    r.recurse_dir_and_callback_if_file(env.get_dotfiles_dir(), restore_file)


def remove_dotfiles_from_file_path(path):
    path_components = path.split("/")
    if "" in path_components:
        path_components.remove("")
    if "Dotfiles" in path_components:
        path_components.remove("Dotfiles")
    return os.path.sep.join(path_components)


def restore_file(path):
    print(f"copying : {path} to: {remove_dotfiles_from_file_path(path)}")
