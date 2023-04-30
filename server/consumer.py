
from kafka import KafkaConsumer
import json

class Consumer():
    
    def __init__(self):
        self.topic = 'temp_change'
        self.consumer = KafkaConsumer(self.topic, value_deserializer=lambda m: json.loads(m.decode('ascii')))

    def consume (self):

        for message in self.consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
