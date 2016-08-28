import ConfigParser
from bs4 import BeautifulSoup as HTML
from datetime import *
import urllib2
from Weather_Forecast import Weather_Forecast


"""This Class Fetches National Weather data from weather.gov."""
class National_Weather_Data():
    def __init__(self):
        self.lat_lng  = {}
        self.url = ''
        self.total_locations= 0
        self.current = 0


    """Gets all Coordinates to determine weather and update total number of locations
    @updates self.lat_lng
        Dictionary of lat: lng
    @updates self.total_locations"""
    def getAllCoordinates(self):
        with open('../DATA/DATA_IN/lat_lng') as city_data_file:
            for city_data in city_data_file:
                city_data = city_data.split(',')
                lat = city_data[3]
                lng = city_data[4].strip('\n')
                self.lat_lng[lat] = lng
        self.total_locations = len(self.lat_lng.keys())


    """Sets self.url with path in config file
    @updates self.url"""
    def setURL(self):
        config = ConfigParser.ConfigParser()
        config.read('../CONFIG/CONFIG.ini')
        self.url = (config.get('URL', 'forecast'))

    """Gets base url to parse
    @param lat
        latitude to replace into url
    @param lng
        Longitude to replace into url"""
    def getURL(self,lat, lng):
        url = self.url.replace('latitude', str(lat)).replace('longitude', str(lng))
        return url


    """Gets Weather Information and Writes data to file.
    @param url
        url to parse weather for
    @param lat
        latitude of weather forecast
    @param lng
        longitude of weather forecast"""
    def getWeather(self, url, lat, lng):
        weather_data = HTML(urllib2.urlopen(url).read(), 'lxml')
        location = weather_data.html.body.forecast['location']
        time = weather_data.html.body.creationtime.string
        weather = weather_data.html.body.contents[0].contents[4]
        weather_forecast = Weather_Forecast(lat, lng, location, time)
        weather_forecast.detWeatherProperties(weather)
        weather_forecast.outputWeatherProperties()
        print url


    """Records Weather data for lat,lng coordinate
    @updates self.current
        current location number"""
    def processWeatherData(self):
        for lat, lng in self.lat_lng.items():
            url = self.getURL(lat, lng)
            try:
                self.getWeather(url, lat, lng)
            except:
                pass
            self.current += 1
            print str(self.current) + ' of ' + str(self.total_locations)
            print '!' * 20


    """Fetches and records weather data for geographic locations in ../DATA/DATA_IN/lat_lng"""
    def fetchWeatherData(self):
        self.getAllCoordinates()
        self.setURL()
        self.processWeatherData()


if __name__ == '__main__':
    start = datetime.now()
    Weather = National_Weather_Data()
    Weather.fetchWeatherData()
    end = datetime.now()
    print end-start