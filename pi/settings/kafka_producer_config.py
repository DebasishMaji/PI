from ..settings import *
import yaml
from .kafka_config import KafkaConfig


class KafkaProducerConfig(KafkaConfig):
    def __init__(self):
        super(KafkaProducerConfig, self).__init__()
        self.producer_cfg = None
        self.parse_config()

    def parse_config(self):
        with open(self.BASE_DIR + "/config/kafka_producer_config.yml", 'r') as producer_yml_file:
            self.producer_cfg = yaml.load(producer_yml_file)

    def fetch_config(self):
        for section in self.producer_cfg:
            PILogger.info(section)
        PILogger.info(self.producer_cfg['kafka'])

        return self.producer_cfg['kafka']

