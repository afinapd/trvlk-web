import os
import json

class Config(object):
    """Simple singleton class for managing and accessing helper"""

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setting.json')) as f:
            setting = json.load(f)
            # self.url = setting['url']
            self.browser = setting['browser']
            self.driver_timeout = int(setting['driver_timeout'])
            self.wait_time = setting['wait_time']

config = Config()