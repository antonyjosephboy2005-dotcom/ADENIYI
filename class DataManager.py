class DataManager:

    def __init__(self):
        self.all_zones = {}

    def register_zone(self, zone_obj):
        self.all_zones[zone_obj.name] = zone_obj

    def calculate_zone_averages(self, zone_name):
        """Aggregate daily averages per sensor zone."""
        target_zone = self.all_zones.get(zone_name)

        if not target_zone:
            return None

        total_val = 0
        count = 0

        for s_id in target_zone.sensor_list:
            sensor = target_zone.sensor_list[s_id]
            for m in sensor.records:
                total_val += m.value
                count += 1

        if count == 0:
            return 0

        return total_val / count
        
        if count == 0:
            return 0
        return total_val / count