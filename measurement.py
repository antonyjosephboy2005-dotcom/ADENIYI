from datetime import datetime

class Measurement:
    def __init__(self, value):
        self.value = value
        self.timestamp = datetime.now()
