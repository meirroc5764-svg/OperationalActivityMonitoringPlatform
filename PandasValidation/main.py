import logging
from logger import logger
from Producer import MyProducer
from Consumer import MyConsumer
from Validation import PandasServers

logger = logging.getLogger(__name__)




config = {
    "bootstrap.servers" : "localhost:9092",
    "GroupId": "pGroop"
    }

consumer = MyConsumer(config)
producer = MyProducer(config)
ps = PandasServers()

while True:

    message = consumer.read_Kafka("activity-readings")

    if message == None:
        logger.info("the massage is Empty or invalid")
        continue

    result = ps.calculation(message)

    if result == None:
        logger.info("invalid data")
        continue

    
    producer.Write_kafka("topic2", result)

    












