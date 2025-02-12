import datetime

class Tyre:
    def __init__(self):
        self.readings = []

    def take_reading(self, pressure, tread_depth):
        timestamp = datetime.datetime.today()
        reading = { "timestamp": timestamp, "pressure": pressure, "tread_depth": tread_depth }
        self.readings.append(reading)

    def get_latest_reading(self):
        return self.readings[0]