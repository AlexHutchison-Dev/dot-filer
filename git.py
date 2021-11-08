"""
    This module is responcible for the programs git intergrations.
"""
import os
import filecmp
import file_helpers as fh
import envvars


def git_module():
    check_for_git_repo()
    print("\n\n In Git Module \n\n")
    modified_files = check_dotfiles_for_modifications()
    copy_modified_files(modified_files)


def check_for_git_repo():
    if os.path.exists(envvars.dotfiles_dir() + "/.git"):
        return
    else:
        initialize_git_repo()


def initialize_git_repo():
    print("no git repo, Initializing now.")


def check_dotfiles_for_modifications():
    files_up_to_date = True
    outdated_files = []
    lines = fh.read_register_by_line(fh.open_register_for_reading())
    for line in lines:
        line = line.replace("\n", "")
        if not diff_stored_and_current_files(line):
            outdated_files.append(line)
    print("Files up to date: {}".format(files_up_to_date))
    return outdated_files


def diff_stored_and_current_files(path):
    return filecmp.cmp(envvars.dotfiles_dir() + path, os.environ["HOME"] + path)


def copy_modified_files(files):
    for file in files:
        print(
            "copying {} to {}".format(
                os.environ["HOME"] + file, envvars.dotfiles_dir() + file
            )
        )
        fh.copy_file(os.environ["HOME"] + file, envvars.dotfiles_dir() + file)
