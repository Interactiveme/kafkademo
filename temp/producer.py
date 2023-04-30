from kafka import KafkaProducer
import json

class Sender():
    
    def __init__(self):
        self.topic = 'temp_change'
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'), bootstrap_servers='localhost:9092')

    def send (self, payload):
        self.producer.send(self.topic, payload)












