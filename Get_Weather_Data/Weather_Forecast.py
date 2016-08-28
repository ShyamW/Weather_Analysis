<<<<<<< HEAD
"""Class Used to Represent parsed Weather in a standardized way.
@author
    Shyam Thiagarajan"""
=======
"""This class is used to standardize the way weather data is recorded.
@author Shyam Thiagarajan"""

>>>>>>> 16fda4c01bcd199183dcccf0e06939414a00b914
class Weather_Forecast():
    def __init__(self, lat, lng, location, time):
        self.temperature = 0
        self.forecast = 'NO WEATHER'
        self.precipitation_chance = 0
        self.location = location
        self.LAT = lat
        self.LNG = lng
        self.day = 'Sunday'
        self.time = time

    """Determines Weather Properties from XML table.
    @param self
        Weather_Forecast Object
    @param weather_table
        XML tag containing weather data
    @replaces self.forecast
    @replaces self.day
    @replaces self.temperature
    @replaces self.precipitation_chance"""
    def detWeatherProperties(self, weather_table):
        self.forecast = weather_table.weather.string
        self.day = weather_table.valid.string
        self.temperature = weather_table.temp.string
        try:
            self.precipitation_chance = weather_table.pop.string
        except Exception:
            print 'Exception'

    """Writes Weather Properties to text file
    @param self
        Weather Forecast Object"""
    def outputWeatherProperties(self):
        out = open('../DATA/DATA_OUT/weather_out', 'a')
        out.write('Latitude: ' + self.LAT)
        out.write(', Longitude: ' + self.LNG)
        out.write(', Day: ' + self.day)
        out.write(', Time: ' + self.time)
        out.write(', Temperature: ' + str(self.temperature))
        out.write(', Forecast' + self.forecast)
        out.write(', Chance of Precipitation: ' + str(self.precipitation_chance))
        out.write(', Location: ' + self.location + '\n')

