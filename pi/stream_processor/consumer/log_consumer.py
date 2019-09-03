from pi import KafkaConsumerClient
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pi.settings.base_config import BaseConfig


class LogConsumer(object):
    # TODO: Implement parallel processing
    def __init__(self):
        self.kafka_consumer_client = KafkaConsumerClient()
        self.spark_context = SparkContext(appName="SparkStreamingKafka")
        self.spark_context.setLogLevel("WARN")
        self.config = BaseConfig()
        self.consumer_config = self.config.fetch_consumer_config()
        self.spark_streaming_context = StreamingContext(self.spark_context, self.consumer_config.get("TIMER"))
        self.kafkaStream = KafkaUtils.createStream(self.spark_streaming_context,
                                              self.consumer_config["zookeeper"],
                                              self.consumer_config["kafka"]["group_id"],
                                              {self.consumer_config["kafka"]["kafka_topic"]: 1})

    def stream_data(self):
        self.kafka_consumer_client.consume_message()

    def stream_data_through_spark(self):
        lines = self.kafkaStream.map(lambda x: x[1])
        for line in lines:
            print(line)
        self.spark_streaming_context.start()
        self.spark_streaming_context.awaitTermination()

