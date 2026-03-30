import configparser
import os


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.parser = configparser.ConfigParser()
            config_path = os.path.join(os.path.dirname(__file__), "../../config.ini")
            cls._instance.parser.read(config_path)
        return cls._instance

    def get(self, section, option):
        return self.parser.get(section, option)
