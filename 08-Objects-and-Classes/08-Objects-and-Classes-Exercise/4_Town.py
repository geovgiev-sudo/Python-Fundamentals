class Town:

    def __init__(self, name: str):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
##################
class Town:

    def __init__(self,name:str):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
