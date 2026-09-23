from pathlib import Path
from confluent_kafka import Producer

config = {"bootstrap.servers" : "localhost:9092"}

producer = Producer(config)

file_name = "activity_readings.csv"

path = next(Path("c:/").rglob(file_name))
print(path)

with open(path, "r", encoding="utf-8") as f:
    all_data = f.readlines()

count = 0
for data in all_data:

    try:
        data = data

        producer.produce("activity-readings",data)
        count += 1
        print("send to kafka")

    except Exception as e:
        print(f"you have {e.args} exepsion")

print(f"send {count} message to kafka")

