from measurement import Measurement

class Sensor:
    def __init__(self, sensor_id, sensor_type):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.measurements = []

    def record(self, value):
        measurement = Measurement(value)
        self.measurements.append(measurement)
