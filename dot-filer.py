#!/usr/bin/env python3
import sys
import os
from shutil import copyfile


def main():

    print("Running")
    dotfiles_path = os.environ["HOME"] + "/dotfiles"
    file = check_for_file(sys.argv[1])

    check_for_dotfiles_directory(dotfiles_path)
    # Check the file provided by the user exists and if not create it
    if file["exists"]:
        add_file(file["file"])
    else:
        add_file(file["file"])


def check_for_file(file):
    exists = False
    if "/" in file:
        if os.path.exists(file):
            exists = True
    elif os.path.exists(os.getcwd() + "/" + file):
        # TODO add file
        file = os.getcwd() + "/" + file
        exists = file

    return {"exists": exists, "file": file}


def add_file(file_path):
    print("Adding file: {}".format(file_path))


def copy_file(src, dest):
    size = os.stat(src).st_size
    print(size)
    copyfile(src, dest)
    # TODO complet this


def check_for_dotfiles_directory(path):
    if os.path.exists(path):
        print("dot-filer directory exists")
    else:
        os.mkdir(path)


if __name__ == "__main__":
    main()
