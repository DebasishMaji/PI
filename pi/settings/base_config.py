import os
import logging
import sys

PILogger = logging.getLogger("PILogger")
PILogger.setLevel(logging.INFO)
FORMAT = '[%(asctime)s %(levelname)s %(threadName)s] %(name)s: %(message)s'
logging.basicConfig(stream=sys.stdout, format=FORMAT)


class BaseConfig(object):

    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        super(BaseConfig, self).__init__()