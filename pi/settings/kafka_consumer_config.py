import yaml
from .kafka_config import *


class KafkaConsumerConfig(KafkaConfig):
    def __init__(self):
        self.consumer_cfg = None
        super(KafkaConsumerConfig, self).__init__()

    def parse_config(self):
        with open(self.BASE_DIR + "/config/kafka_consumer_config.yml", 'r') as consumer_yml_file:
            self.consumer_cfg = yaml.load(consumer_yml_file)

    def fetch_config(self):
        for section in self.consumer_cfg:
            self.PILogger.info(section)
        self.PILogger.info(self.consumer_cfg['kafka'])

        return self.consumer_cfg['kafka']
