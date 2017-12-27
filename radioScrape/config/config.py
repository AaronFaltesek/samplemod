import os
import yaml

class AppConfig():
    '''
    Set config values from yml file
    '''
    def __init__(self):
        cfg_list = {}
        print("Initialized appconfig")

    def get_config_item(self,key):
        return self.cfg_list["default"][key]


    def set_config_yml(self):
        configLoc = os.path.join(os.path.abspath(os.path.dirname(__file__)),'config.yaml')
        with open(configLoc, 'r') as stream:
            try:
                self.cfg_list = yaml.load(stream)
                print(self.cfg_list)
                print(self.cfg_list["default"]["mp3_repo_base"])
                print("-")
            except yaml.YAMLError as exc:
                print(exc)


    