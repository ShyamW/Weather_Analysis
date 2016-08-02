class Weather_Forecast():
    def __init__(self, lat, lng):
        self.humidity = ''
        self.wind_speed = ''
        self.wind_pressure = ''
        self.dew_point = ''
        self.visibility = ''
        self.heat_index = ''
        self.last_update = ''
        self.LAT = lat
        self.LNG = lng


    """Determines Weather Properties.
    @param self
        Weather_Forecast Object
    @param weather_table
        HTML table containing weather data
    @replaces self.humidity
    @replaces self.wind_speed
    @replaces self.wind_pressure
    @replaces self.dew_point
    @replaces self.visibility
    @replaces self.heat_index
    @replaces self.last_update"""
    def detWeatherProperties(self, weather_table):
        HUMIDITY_INDEX = 1
        WIND_SPEED_INDEX = 3
        WIND_PRESSURE_INDEX = 5
        DEW_POINT_INDEX = 7
        VISIBILITY_INDEX = 9
        HEAT_INDEX_INDEX = 11
        LAST_UPDATE_INDEX = len(weather_table.contents)-1
        self.humidity = str(weather_table.contents[HUMIDITY_INDEX].contents[3].string)
        self.wind_speed = str(weather_table.contents[WIND_SPEED_INDEX].contents[3].string)
        self.wind_pressure = str(weather_table.contents[WIND_PRESSURE_INDEX].contents[3].string)
        self.dew_point = weather_table.contents[DEW_POINT_INDEX].contents[3].string.encode('utf-8')
        self.visibility = str(weather_table.contents[VISIBILITY_INDEX].contents[3].string)
        try:
            self.heat_index = weather_table.contents[HEAT_INDEX_INDEX].contents[1].string.encode('utf-8')
        except:
            print 'No Heat'
        try:
            self.last_update = str(weather_table.contents[LAST_UPDATE_INDEX].contents[3].string).lstrip().rstrip()
        except:
            self.last_update = str(weather_table.contents[LAST_UPDATE_INDEX].string).lstrip().rstrip()


    """Writes Weather Properties to text file
    @param self
        Weather Forecast Object"""
    def outputWeatherProperties(self):
        out = open('weather_out', 'a')
        out.write(' LAT: ' + self.LAT)
        out.write(' LNG: ' + self.LNG)
        out.write(' Humidity: ' + self.humidity)
        out.write(' Wind Speed: ' + self.wind_speed)
        out.write(' Wind Pressure: ' + self.wind_pressure)
        out.write(' Dew Point: ' + self.dew_point)
        out.write(' Visibility: ' + self.visibility)
        out.write(' Heat Index: ' + self.heat_index)
        out.write(' Last Updated: ' + self.last_update + '\n')
        out.write('*' * 50 + '\n')
