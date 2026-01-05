class Forecaster:

    @staticmethod
    def predict_trend(sensor_obj):
        """Predict future readings using simple extrapolation."""
        data = sensor_obj.records

        if len(data) < 2:
            return "Not enough data to predict."

        current = data[-1].value
        previous = data[-2].value
        diff = current - previous
        prediction = current + diff

        return prediction