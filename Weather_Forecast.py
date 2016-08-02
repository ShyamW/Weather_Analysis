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


    def detWeatherProperties(self, weather_table):
        HUMIDITY_INDEX = 1
        WIND_SPEED_INDEX = 3
        WIND_PRESSURE_INDEX = 5
        DEW_POINT_INDEX = 7
        VISIBILITY_INDEX = 9
        HEAT_INDEX_INDEX = 11
        LAST_UPDATE_INDEX = 13
        self.humidity = str(weather_table.contents[HUMIDITY_INDEX].contents[3].string)
        self.wind_speed = str(weather_table.contents[WIND_SPEED_INDEX].contents[3].string)
        self.wind_pressure = str(weather_table.contents[WIND_PRESSURE_INDEX].contents[3].string)
        self.dew_point = weather_table.contents[DEW_POINT_INDEX].contents[3].string.encode('utf-8')
        self.visibility = str(weather_table.contents[VISIBILITY_INDEX].contents[3].string)
        self.heat_index = weather_table.contents[HEAT_INDEX_INDEX].contents[1].string.encode('utf-8')
        print weather_table.contents
        print len(weather_table.contents)
        self.last_update = str(weather_table.contents[LAST_UPDATE_INDEX].contents[3].string).lstrip().rstrip()

    def outputWeatherProperties(self):
        print self.LAT
        print self.LNG
        print 'Humidity: ' + self.humidity
        print 'Wind Speed: ' + self.wind_speed
        print 'Wind Pressure: ' + self.wind_pressure
        print 'Dew Point: ' + self.dew_point
        print 'Visibility: ' + self.visibility
        print 'Heat Index: ' + self.heat_index
        print 'Last Updated: ' + self.last_update
        print '*' * 50
