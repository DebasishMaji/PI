import yaml
from .kafka_config import KafkaConfig


class KafkaConsumerConfig(KafkaConfig):
    def __init__(self):
        super(KafkaConsumerConfig, self).__init__()
        self.consumer_cfg = None

    def fetch_config(self):
        self.parse_consumer_config()
        return self.consumer_cfg['kafka']
