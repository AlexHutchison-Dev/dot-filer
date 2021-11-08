import os
import envvars


def startup_checks():
    check_register_file_exists()


def check_register_file_exists():
    print("in setup")
    if os.path.exists(envvars.register_path()):
        print("dotfile.txt exists yo!")
        return
    else:
        create_dotfiles_register()


def create_dotfiles_register():
    cwd = os.getcwd()
    os.chdir(os.environ["HOME"] + "/.local/bin/")
    f = open("dotfiles.txt", "x")
    f.close()
    os.chdir(cwd)
