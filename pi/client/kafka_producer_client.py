from .kafka_client import *
from ..settings import *
from kafka import KafkaProducer
import json


class KafkaProducerClient(KafkaClient):
    def __init__(self):
        self.kafka_consumer_client = None
        producer_config = KafkaProducerConfig()
        self.kafka_producer_config = producer_config.fetch_config()
        self.kafka_producer = KafkaProducer(bootstrap_servers=self.kafka_producer_config.get("bootstrap_servers"),
                                            value_serializer=lambda x: json.dumps(x).encode('utf-8'), api_version=(0, 10, 1))
        super(KafkaProducerClient, self).__init__()

    def get_client(self):
        return self.kafka_producer

    def send_message(self, data=None, message_type='json'):
        # TODO: different  message_type support needs to be implemented

        if message_type == 'json':
            self.kafka_producer.send(self.kafka_producer_config["kafka_topic"], json.dumps(data)).add_callback(self.send_success_callback).add_errback(self.send_error_errorback)
            self.kafka_producer.flush()

    def send_message_async(self, data=None, message_type='json'):
        # TODO: Yet to be implemented
        raise NotImplementedError("Yet to be implemented")

    @staticmethod
    def send_success_callback(record_metadata):
        PILogger.info("Topic: %s" % record_metadata.topic)
        PILogger.info("Partition: %s" % record_metadata.partition)
        PILogger.info("Offset: %s" % record_metadata.offset)

    @staticmethod
    def send_error_errorback(exc):
        PILogger.error("Error: %s" % exc)
