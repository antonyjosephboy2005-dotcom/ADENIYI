class AlertSystem:
    def __init__(self, threshold):
        self.threshold = threshold

    def check_alert(self, value):
        if value > self.threshold:
            return "⚠ ALERT: Threshold Exceeded!"
        return "Normal"
