#!/usr/bin/env python3
import sys
import setup
import add_files
import git
import os
import envvars_class


def main():
    print(len(sys.argv))
    env = envvars_class.Env()
    print(os.environ["HOME"])
    setup.startup_checks(env)
    if len(sys.argv) >= 3:
        if sys.argv[1] == "-a" or sys.argv[1] == "add":
            print("Running")
            for file in range(2, len(sys.argv)):
                add_files.add_file(sys.argv[file], env)
        elif sys.argv[1] == "-g" or sys.argv[1] == "git":
            git.git_module(env)

    else:
        print("usage dot-filer -a <file name>")


if __name__ == "__main__":
    main()


