 ____        _     _____ _ _
|  _ \  ___ | |_  |  ___(_) | ___ _ __
| | | |/ _ \| __| | |_  | | |/ _ \ '__|
| |_| | (_) | |_  |  _| | | |  __/ |
|____/ \___/ \__| |_|   |_|_|\___|_|

A program to manage your dot files.

## Project Overview

I want this to be a program that will allow a user to maintain a list of their dot files, stored as
the files themselves, but as also paths relative to their home directory.  Idealy this will be able
to up-load/sync the dot files with some remote repository like gitHub over ssh.

With one command I want a user to be able to update their store of current dot files and paths relative
to the home directory.  This should go the other way, where on a new computer or vm restoring
dotfiles should be as easy as: 
    dotfiles <repository-name>

## MVP
 
### Add new file

The program required the functionality to add new files to the dotfiles repository. This process
should go something like this.

  [ ] test that user provided file argument to program
  [ ] check if the user provided full path or just file name
      * if file name: add cwd path to file name, then trim so path is relative to $HOME
      * else : trim path to relative to home directory
  [ ] add full file path to file list log

### Check for file in dotfiles

The program need to be able to check if a file  already exists in the dotfiles storage directory.

  [ ] searh dotfiles directory for file path relative to home
  [ ] return true if file already exists


