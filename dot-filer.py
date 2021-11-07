#!/usr/bin/env python3
import sys
import functions


def main():
    print(len(sys.argv))
    if len(sys.argv) >= 3:
        if sys.argv[1] == "-a" or sys.argv[1] == "add":
            print("Running")
            for file in range(2, len(sys.argv)):
                functions.add_file(sys.argv[file])
    else:
        print("usage dot-filer -a <file name>")


if __name__ == "__main__":
    main()
