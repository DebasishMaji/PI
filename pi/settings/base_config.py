import os
import logging
import sys


class BaseConfig(object):

    def __init__(self):
        self.PILogger = None
        self.setup_logger()
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    def setup_logger(self):

        FORMAT = '[%(asctime)s %(levelname)s %(threadName)s] %(name)s: %(message)s'
        logging.basicConfig(stream=sys.stdout, format=FORMAT)
        self.PILogger = logging.getLogger("PILogger")
        self.PILogger.setLevel(logging.INFO)
