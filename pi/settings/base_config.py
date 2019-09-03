import os
import logging
import sys
import yaml

PILogger = logging.getLogger("PILogger")
PILogger.setLevel(logging.INFO)
FORMAT = '[%(asctime)s %(levelname)s %(threadName)s] %(name)s: %(message)s'
logging.basicConfig(stream=sys.stdout, format=FORMAT)


class BaseConfig(object):

    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        super(BaseConfig, self).__init__()
        self.consumer_cfg = None
        self.producer_cfg = None
        self.parse_consumer_config()
        self.parse_producer_config()

    def parse_consumer_config(self):
        with open(self.BASE_DIR + "/config/kafka_consumer_config.yml", 'r') as consumer_yml_file:
            self.consumer_cfg = yaml.load(consumer_yml_file, Loader=yaml.FullLoader)

    def parse_producer_config(self):
        with open(self.BASE_DIR + "/config/kafka_producer_config.yml", 'r') as producer_yml_file:
            self.producer_cfg = yaml.load(producer_yml_file, Loader=yaml.FullLoader)

    def fetch_consumer_config(self):
        PILogger.info(self.consumer_cfg)
        return self.consumer_cfg

    def fetch_producer_config(self):
        PILogger.info(self.producer_cfg)
        return self.producer_cfg
