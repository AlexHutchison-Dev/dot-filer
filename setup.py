import os
import envvars


def startup_checks(env_instance):
    env = env_instance
    check_dotfiles_dir_exists(env)
    check_register_file_exists(env)


def check_register_file_exists(env):
    if os.path.exists(env.get_register_path()):
        return
    else:
        create_dotfiles_register(env)


def check_dotfiles_dir_exists(env):
    if os.path.exists(env.get_dotfiles_dir()):
        return
    else:
        create_dotfiles_dir(env)


def create_dotfiles_register(env):
    cwd = os.getcwd()
    print(env.get_dotfiles_dir())
    os.chdir(env.get_dotfiles_dir())
    f = open("dotfiles.txt", "x")
    f.close()
    os.chdir(cwd)


def create_dotfiles_dir(env):
    os.mkdir(env.get_dotfiles_dir())
