# A Class to store environment variables and manage there values based on the operating system ##
import os


class Env:
    dotfiles_path = ""
    register_path = ""
    platform = ""
    git_repo_uri = "git@github.com:AlexHutchison-Dev/Dotfiles.git"

    def __init__(self):
        self.setup_environment_variables()

    def setup_environment_variables(self):
        self.dotfiles_path = os.path.join(os.environ["HOME"], "Dotfiles")
        self.register_path = os.path.join(
            os.environ["HOME"], "Dotfiles", "dotfiles.txt"
        )

    def get_dotfiles_dir(self):
        return self.dotfiles_path

    def get_register_path(self):
        return self.register_path

    def get_git_repo_uri(self):
        return self.git_repo_uri
