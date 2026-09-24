import logging
from logger import logger
from confluent_kafka import Producer
import json

logger = logging.getLogger(__name__)


class MyProducer:
    def __init__(self, config):
        self.producer = Producer(config)

    def Write_kafka(self, topic, message):
        logger.info("start write to kafka ...")

        try:

            self.producer.produce(topic, message)

            logger.info(f"write to topic {topic}")

        except Exception as e:
            logger.error(f"write to kafka false")
            





        