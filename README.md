# ADENIYI
OOP HMEWORK
1. Sensor Class
The Sensor class represents a physical device used to collect environmental data such as
temperature, air quality, or water quality. It is responsible for identifying the sensor, knowing what
type of data it measures, and producing measurements.
Typical attributes include sensorId, type, unit, and zone. Typical methods include taking a
measurement and returning sensor information.
2. Measurement Class
The Measurement class represents a single data reading collected from a sensor. Each
measurement contains a value, a timestamp, and the ID of the sensor that produced it. Separating
measurements from sensors allows historical data analysis and trend detection.
3. EnvironmentZone Class
The EnvironmentZone class represents a monitored area such as an industrial zone, residential
area, or river basin. It groups sensors and measurements belonging to the same area. It typically
contains a list of sensors and a list of measurements, and methods to add and analyze them.
4. DataLogger Class
The DataLogger class manages data collection and storage. It registers sensors, logs
measurements, and organizes data by zones. This separation improves maintainability and
scalability of the system.
5. AlertSystem Class
The AlertSystem class monitors measurements and generates alerts when values exceed defined
thresholds. It is responsible for environmental safety and early warning notifications.
6. Use of Composition
Composition is used to model “has-a” relationships: EnvironmentZone has sensors and
measurements, Sensor has measurements, DataLogger has zones. This accurately reflects
real-world ownership and lifecycle dependency.
7. Summary of Class Relationships
Sensors generate measurements.
Measurements belong to sensors.
Sensors are grouped into environment zones.
Zones are managed by the data logger.
Alerts are generated based on logged data
