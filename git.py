import os
from datetime import datetime
import file_helpers as fh
import envvars_class

# TODO replace os.system calls with the more advanced methods that allow me to verify that htings
# worked

env = envvars_class.Env()


def git_module():
    print("\n\n In Git Module \n\n")
    copy_modified_files(check_dotfiles_for_modifications())
    perform_git_add()
    perform_git_commit()
    perform_git_push()


def get_local_staus_relative_to_remote():
    output = os.popen("git remote show origin").read()
    print(f"output: {output}")
    if "(fast-forwardable)" in output:
        return "ahead"
    elif "(local out of date)" in output:
        return "behind"
    return


def check_for_git_repo():
    if os.path.exists(env.get_dotfiles_dir() + "/.git"):
        return
    else:
        create_git_repo()


def create_git_repo():
    initialize_git_repo()
    add_git_remote_origin_url()


# TODO Consider refactoring out this change directory logic it repeats
def initialize_git_repo():
    cwd = os.getcwd()
    print(env.get_dotfiles_dir())
    os.chdir(env.get_dotfiles_dir())
    os.system("git init")
    os.chdir(cwd)


def add_git_remote_origin_url():
    cwd = os.getcwd()
    print("adding remote url: {}".format(env.get_git_repo_uri()))
    os.chdir(env.get_dotfiles_dir())
    os.system("git remote add origin {}".format(env.get_git_repo_uri()))
    os.chdir(cwd)

#TODO This function too long and toomany levels of abstraction
def check_dotfiles_for_modifications():
    files_up_to_date = True
    outdated_files = []
    lines = fh.read_register_by_line(
        fh.open_register_for_reading(env.get_register_path())
    )
    for line in lines:
        line = line.replace("\n", "")
        if not fh.diff_stored_and_current_files(fh.path_relative_to_home(line)):
            outdated_files.append(line)
    print("Files up to date: {}".format(files_up_to_date))
    return outdated_files


def copy_modified_files(files):
    for file in files:
        print(
            "copying {} to {}".format(
                os.environ["HOME"] + file, env.get_dotfiles_dir() + file
            )
        )
        fh.copy_file(os.environ["HOME"] + file, env.get_dotfiles_dir() + file)


def perform_git_add():
    cwd = os.getcwd()
    os.chdir(env.get_dotfiles_dir())
    os.system("git add .")
    os.chdir(cwd)


def perform_git_commit():
    cwd = os.getcwd()
    os.chdir(env.get_dotfiles_dir())
    print("git commit -m {}".format(datetime.today().strftime("%Y-%m-%d-%H:%M:%S")))
    commit_message = "git commit -m {}".format(
        datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
    )
    os.system(commit_message)
    os.chdir(cwd)


def perform_git_push():
    cwd = os.getcwd()
    os.chdir(env.get_dotfiles_dir())
    os.system("git push origin master")
    os.chdir(cwd)
