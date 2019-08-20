from ..settings import *
import yaml
from .kafka_config import KafkaConfig


class KafkaConsumerConfig(KafkaConfig):
    def __init__(self):
        super(KafkaConsumerConfig, self).__init__()
        self.consumer_cfg = None
        self.parse_config()

    def parse_config(self):
        with open(self.BASE_DIR + "/config/kafka_consumer_config.yml", 'r') as consumer_yml_file:
            self.consumer_cfg = yaml.load(consumer_yml_file)

    def fetch_config(self):
        for section in self.consumer_cfg:
            PILogger.info(section)
        PILogger.info(self.consumer_cfg['kafka'])

        return self.consumer_cfg['kafka']
