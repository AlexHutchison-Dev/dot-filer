import os
import envvars_class
import git

env = envvars_class.Env()


def startup_checks():
    check_dotfiles_dir_exists()
    # check_register_file_exists()
    git.check_for_git_repo()


# def check_register_file_exists():
    # if os.path.exists(env.get_register_path()):
    #     return
    # else:
    #     create_dotfiles_register()


def check_dotfiles_dir_exists():
    if os.path.exists(env.get_dotfiles_dir()):
        return
    else:
        create_dotfiles_dir()


# def create_dotfiles_register():
#     cwd = os.getcwd()
#     print(env.get_dotfiles_dir())
#     os.chdir(env.get_dotfiles_dir())
#     f = open("dotfiles.txt", "x")
#     f.close()
#     os.chdir(cwd)


def create_dotfiles_dir():
    os.mkdir(env.get_dotfiles_dir())
