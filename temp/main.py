from producer import Sender
import time

sender = Sender()

for _ in range(100):
    time.sleep(5)
    sender.send({'id': 'temp_sender_1', 'temp': 10})
    sender.send({'id': 'temp_sender_2', 'temp': 12})
