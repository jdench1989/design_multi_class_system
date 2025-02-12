class Tyre:
    
    def __init__(self):
        self.readings = []
        # => [{"timestamp": datetime.now, "pressure": xxxx, "tread_depth": xxxx]}, ...]

    def take_reading(self, pressure, tread_depth):
        # side effect: append reading with timestamp to start of self readings list
        pass

    def get_latest_reading(self):
        return self.readings[0]