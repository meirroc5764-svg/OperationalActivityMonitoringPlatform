from confluent_kafka import Consumer

class MyConsumer:
    def __init__(self, config):
        self.consumer = Consumer(config)

    def read_Kafka(self,topic):
        self.consumer.subscribe(topic)
        try:
            
            result = self.consumer.consume()
            return result

        except Exception as e:
            print(f"you have {e} excepsion")




        