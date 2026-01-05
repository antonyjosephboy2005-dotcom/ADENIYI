import datetime


class AlertSystem:
    def __init__(self, limit):
        self.limit = limit
        self.alert_history = []

    def check_and_trigger(self, val, s_id):
        if val > self.limit:
            msg = f"!!! WARNING !!! Sensor {s_id} hit {val}. Threshold is {self.limit}."
            self.alert_history.append({
                "time": datetime.datetime.now(),
                "status": "ACTIVE",
                "val": val
            })
            print(msg)
        else:
            if len(self.alert_history) > 0 and self.alert_history[-1]["status"] == "ACTIVE":
                print(f"Fixed: Sensor {s_id} is back to normal ({val}).")
                self.alert_history.append({
                    "time": datetime.datetime.now(),
                    "status": "CLEARED",
                    "val": val
                })