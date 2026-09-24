import logging
from pathlib import Path
from logger import logger
from confluent_kafka import Producer

logger = logging.getLogger(__name__)

config = {"bootstrap.servers" : "localhost:9092"}

producer = Producer(config)

file_name = "activity_readings.csv"

path = next(Path("c:/").rglob(file_name))

with open(path, "r", encoding="utf-8") as f:
    all_data = f.readlines()

count = 0
for data in all_data:

    try:
        data = data

        producer.produce("activity-readings",data)
        count += 1
        logger.info("send to kafka")

    except Exception as e:
        logger.error(f"you have {e.args} exepsion")

logger.info(f"send {count} message to kafka")

