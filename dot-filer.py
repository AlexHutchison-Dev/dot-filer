#!/usr/bin/env python3
import sys
import functions


def main():

    print("Running")
    # Should probaly have different location in file system
    file = sys.argv[1]
    functions.check_for_dotfiles_directory()
    # Check the file provided by the users
    if functions.check_for_file(file):
        functions.add_file(file)
    else:
        print("usage dot-filer <file>")
        return 1


if __name__ == "__main__":
    main()
