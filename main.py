from sensor import Sensor
from measurement import Measurement
from environment_zone import EnvironmentZone
from data_logger import DataLogger
from alert_system import AlertSystem

# Setup
zone1 = EnvironmentZone("Industrial Area")
zone2 = EnvironmentZone("Residential Area")

logger = DataLogger()
logger.register_zone(zone1)
logger.register_zone(zone2)

sensor1 = Sensor(1, "Air", zone1)
sensor2 = Sensor(2, "Air", zone2)

zone1.add_sensor(sensor1)
zone2.add_sensor(sensor2)

alert = AlertSystem(threshold=75)

# Simulation
for _ in range(5):
    value = sensor1.read_value()
    m = Measurement(sensor1.sensor_id, value)
    logger.log_measurement("Industrial Area", m)
    print("Industrial:", value, alert.check_alert(value))

for _ in range(5):
    value = sensor2.read_value()
    m = Measurement(sensor2.sensor_id, value)
    logger.log_measurement("Residential Area", m)
    print("Residential:", value, alert.check_alert(value))

# Reports
print("\nDaily Averages:")
for zone in logger.zones:
    print(zone, logger.daily_average(zone))

print("\nHighest Pollution Zones:")
for zone, _ in logger.highest_pollution_zones():
    print(zone)
