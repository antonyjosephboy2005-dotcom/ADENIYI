class EnvironmentZone:
    def __init__(self, name):
        self.name = name
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def get_all_measurements(self):
        values = []
        for sensor in self.sensors:
            for m in sensor.measurements:
                values.append(m.value)
        return values
