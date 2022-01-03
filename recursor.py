import os


def recurse_dir_and_callback_if_file(path, callback):
    print(f"path: {path}")
    if os.path.isdir(path):
        os.chdir(path)

    contents = get_list_of_directory_contents(path)
    print(f"contents: {contents}")
    for content in contents:
        if os.path.isdir(content):
            recurse_dir_and_callback_if_file(
                os.path.join(os.getcwd(), content), callback
            )
        else:
            callback(content)
    return_to_parent_directory()


def get_list_of_directory_contents(path):
    contents = os.listdir(path)
    return remove_git_directory_from_contents_list(contents)


def remove_git_directory_from_contents_list(list):
    if ".git" in list:
        list.remove(".git")
    return list


def return_to_parent_directory():
    current_directories = os.getcwd().split("/")
    del current_directories[-1]
    os.chdir(os.sep.join(current_directories))
