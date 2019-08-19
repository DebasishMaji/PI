from .kafka_client import *
from ..settings.kafka_consumer_config import *
from kafka import KafkaConsumer


class KafkaConsumerClient(KafkaClient):
    def __init__(self):
        self.kafka_consumer_client = None
        consumer_config = KafkaConsumerConfig()
        self.kafka_consumer_config = consumer_config.fetch_config()
        self.kafka_consumer = KafkaConsumer(bootstrap_servers=self.kafka_consumer_config.get("bootstrap_servers"),
                                            auto_offset_reset='earliest')
        self.kafka_consumer.subscribe([self.kafka_consumer_config.get("kafka_topic")])
        super(KafkaConsumerClient, self).__init__()

    def get_client(self):

        return self.kafka_consumer

    def consume_message(self):
        # TODO: Yet to be implemented
        raise NotImplementedError("Yet to be implemented")
