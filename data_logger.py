class DataLogger:
    def daily_average(self, zone):
        values = zone.get_all_measurements()
        if not values:
            return 0
        return sum(values) / len(values)

    def min_max_mean(self, zone):
        values = zone.get_all_measurements()
        if not values:
            return None
        return min(values), max(values), sum(values) / len(values)
