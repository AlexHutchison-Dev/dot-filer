#!/usr/bin/env python3
import sys
import setup
import add_files
import git


def main():
    setup.startup_checks()
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-a" or sys.argv[1] == "add":
            print(f"adding files {sys.argv[2]}")
            for file in range(2, len(sys.argv)):
                add_files.add_file(sys.argv[file])
        elif sys.argv[1] == "-g" or sys.argv[1] == "git":
            print(f"adding files {sys.argv[2]}, {sys.argv[3]}")
            git.git_module()

    else:
        # TODO Need to make a proper error here, that points to help file
        print("usage dot-filer -a <file name>")


if __name__ == "__main__":
    main()
