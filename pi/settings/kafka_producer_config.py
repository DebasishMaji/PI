from ..settings import *
from .kafka_config import KafkaConfig


class KafkaProducerConfig(KafkaConfig):
    def __init__(self):
        super(KafkaProducerConfig, self).__init__()
        self.producer_cfg = None

    def fetch_config(self):
        self.parse_producer_config()
        PILogger.info(self.producer_cfg['kafka'])
        return self.producer_cfg['kafka']

