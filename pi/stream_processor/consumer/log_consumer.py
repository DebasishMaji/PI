from pi import KafkaConsumerClient


class LogConsumer(object):
    # TODO: Implement parallel processing
    kafka_consumer_client = KafkaConsumerClient()
    kafka_consumer_client.consume_message()

