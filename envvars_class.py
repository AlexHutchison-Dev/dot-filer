## A Class to store environment variables and manage there values based on the operating system ##
import sys
import os
class Env:
  dotfiles_path = ""
  register_path = ""
  platform = ""
  def __init__(self):
    print("Env class os value ")
    self.setup_environment_variables()
  

  def setup_environment_variables(self):
    print(os.environ["HOME"])
    home =os.environ["HOME"]
    self.dotfiles_path = os.path.join(home , "Dotfiles")
    self.register_path = os.path.join(home , "Dotfiles", "dotfiles.txt")

  def get_dotfiles_dir(self):
    print(self.dotfiles_path)
    return self.dotfiles_path  
  
  
  def get_register_path(self):
    print(self.register_path)
    return self.register_path