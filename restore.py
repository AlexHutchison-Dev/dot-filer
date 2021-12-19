# this module is to go through all the files stored in the dotfiles directory and insert them into
# the file system in the correct inplace with the users home directory in place of the Dotfiles
# directory

import os
import envvars_class
import file_helpers as fh

env = envvars_class.Env()

def restore(path = env.get_dotfiles_dir()):
    if os.path.isdir(path):
        os.chdir(path)        
    contents = get_list_of_directory_contents(path)
    for content in contents:
        if os.path.isdir(content):
            restore(os.path.join (os.getcwd(),content))
        else:
           restore_file(os.path.join(os.getcwd(), content)) 
    return_to_parent_directory()


def remove_git_directory_from_list(target_list):
    if ".git" in target_list: 
        target_list.remove(".git")
    return target_list


def get_list_of_directory_contents(path):

    contents = os.listdir(path)
    contents = remove_git_directory_from_list(contents)
    return contents


def remove_dotfiles_from_file_path(path):
    path_components = path.split("/")
    path_components.remove("")
    if "Dotfiles" in path_components:
        path_components.remove("Dotfiles")
    return os.path.sep.join(path_components)


def restore_file(path):
    print(f'copying : {path} to: {remove_dotfiles_from_file_path(path)}')


def return_to_parent_directory():
    current_directories = os.getcwd().split("/" )
    del current_directories[-1]
    os.chdir(os.sep.join(current_directories))
