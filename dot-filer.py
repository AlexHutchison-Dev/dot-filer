#!/usr/bin/env python3
import sys
import functions


def main():

    print("Running")
    # Should probaly have different location in file system
    file = sys.argv[1]
    functions.add_file(file)


if __name__ == "__main__":
    main()
