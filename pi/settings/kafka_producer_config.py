import yaml
from .kafka_config import *


class KafkaConsumerConfig(KafkaConfig):
    def __init__(self):
        self.producer_cfg = None
        super(KafkaConsumerConfig, self).__init__()

    def parse_config(self):
        with open(self.BASE_DIR + "/config/kafka_producer_config.yml", 'r') as consumer_yml_file:
            self.producer_cfg = yaml.load(consumer_yml_file)

    def fetch_config(self):
        for section in self.producer_cfg:
            self.PILogger.info(section)
        self.PILogger.info(self.producer_cfg['kafka'])

        return self.producer_cfg['kafka']

