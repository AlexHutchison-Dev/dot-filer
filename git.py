"""
    This module is responcible for the programs git intergrations.
"""
import os
import filecmp
from datetime import datetime
import file_helpers as fh
import envvars_class

# TODO replace os.system calls with the more advanced methods that allow me to verify that htings
# worked

env = envvars_class.Env()

def git_module():
    check_for_git_repo()
    print("\n\n In Git Module \n\n")
    copy_modified_files(check_dotfiles_for_modifications())
    git_add_in_dotfiles_dir()
    git_commit()
    git_push()


def check_for_git_repo():
    if os.path.exists(env.get_dotfiles_dir() + "/.git"):
        return
    else:
        create_git_repo()


def create_git_repo():
    initialize_git_repo()
    add_git_remote_origin_url()


def initialize_git_repo():
    cwd = os.getcwd()
    print(env.get_dotfiles_dir())
    os.chdir(env.get_dotfiles_dir())
    os.system("git init")
    os.chdir(cwd)


def add_git_remote_origin_url():
    cwd = os.getcwd()
    print("adding remote url: {}".format(envvars.git_repo_remote_url))
    os.chdir(env.get_dotfiles_dir())
    os.system("git remote add origin {}".format(envvars.git_repo_remote_url))
    os.chdir(cwd)


def check_dotfiles_for_modifications():
    files_up_to_date = True
    outdated_files = []
    lines = fh.read_register_by_line(fh.open_register_for_reading(env.get_register_path()))
    for line in lines:
        line = line.replace("\n", "")
        if not diff_stored_and_current_files(line):
            outdated_files.append(line)
    print("Files up to date: {}".format(files_up_to_date))
    return outdated_files


def diff_stored_and_current_files(path):
    return filecmp.cmp(env.get_dotfiles_dir() + path, os.environ["HOME"] + path)


def copy_modified_files(files):
    for file in files:
        print(
            "copying {} to {}".format(
                os.environ["HOME"] + file, env.get_dotfiles_dir() + file
            )
        )
        fh.copy_file(os.environ["HOME"] + file, env.get_dotfiles_dir() + file)


def git_add_in_dotfiles_dir():
    cwd = os.getcwd()
    os.chdir(env.get_dotfiles_dir())
    os.system("git add .")
    os.chdir(cwd)


def git_commit():
    cwd = os.getcwd()
    os.chdir(env.get_dotfiles_dir())
    print("git commit -m {}".format(datetime.today().strftime("%Y-%m-%d-%H:%M:%S")))
    commit_message = "git commit -m {}".format(
        datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
    )
    os.system(commit_message)
    os.chdir(cwd)


def git_push():
    cwd = os.getcwd()
    os.chdir(env.get_dotfiles_dir())
    os.system("git push origin master")
    os.chdir(cwd)
