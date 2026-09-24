import logging
from logger import logger
from confluent_kafka import Consumer
import json

logger = logging.getLogger(__name__)


class MyConsumer:
    def __init__(self, config):
        self.consumer = Consumer(config)

    def read_Kafka(self,topic):
        self.consumer.subscribe(topic)
        try:

            result = self.consumer.poll(5)

            if result == None:
                logger.info("no have message")
                return None 

            if result.error():
                logger.warning(f"you have Error: {result.error}")


            message = json.loads(result.value().decode("utf-8"))

            return message

        except Exception as e:
            logger.error(f"you have {e} excepsion")




        