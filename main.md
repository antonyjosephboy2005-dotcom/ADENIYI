from sensor import Sensor
from environment_zone import EnvironmentZone
from data_logger import DataLogger
from alert_system import AlertSystem

zone = EnvironmentZone("City Center")

sensor1 = Sensor(1, "Air Quality")
sensor2 = Sensor(2, "Temperature")

zone.add_sensor(sensor1)
zone.add_sensor(sensor2)

sensor1.record(80)
sensor1.record(95)
sensor2.record(30)

logger = DataLogger()
alert = AlertSystem(threshold=90)

avg = logger.daily_average(zone)
print("Daily average:", avg)

print(alert.check_alert(avg))
