# A Class to store environment variables and manage there values based on the operating system ##
import os


class Env:
    dotfiles_path = ""
    config_path = ""
    git_repo_uri = "git@github.com:AlexHutchison-Dev/Dotfiles.git"

    def __init__(self):
        self.setup_environment_variables()

    def setup_environment_variables(self):
        self.dotfiles_path = os.path.join(os.environ["HOME"], "Dotfiles")
        self.config_path = os.path.join(
            os.environ["HOME"], ".config", "dot-filer", "config"
        )
        if self.check_for_config_file():
            self.retrieve_git_uri()
        else:
            self.prompt_user_for_git_uri()

    def get_dotfiles_dir(self):
        return self.dotfiles_path

    def get_config_path(self):
        return self.config_path

    def get_git_repo_uri(self):
        return self.git_repo_uri

    def check_for_config_file(self):
        return os.path.exists(self.config_path)

    def retrieve_git_uri(self):
        config = open(self.config_path, "r+") 
        for line in config:
            if "git_repo_uri" in line:
                return line.replace("git_repo_uri:","")

    def prompt_user_for_git_uri(self):
        uri = input("Please enter uri for remote git repository: ")
        self.write_uri_to_config(uri)


    def write_uri_to_config(self, uri):
        print(f'Writing uri to config file: {uri}')
        f = open(self.config_path, 'w+')
        f.write(f'git_repo_uri:{uri}')
        f.close()
        return
