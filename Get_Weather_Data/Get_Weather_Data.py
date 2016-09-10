import ConfigParser
import requests
from Weather_Forecast import Weather_Forecast
from bs4 import BeautifulSoup as HTML

"""Class used to parse and record national weather data"""
class NationalWeather(object):
    def __init__(self):
        self.lat_lng = []
        self.weather_forecasts = []
        print('Fetching')

    """Gets all Coordinates to determine weather for
    @return lat_lng
        Dictionary of lat: lng"""
    def getAllCoordinates(self):
        self.lat_lng = {}
        with open('../DATA/DATA_IN/lat_lng') as city_data_file:
            for city_data in city_data_file:
                city_data = city_data.split(',')
                lat = city_data[3]
                lng = city_data[4].strip('\n')
                self.lat_lng[lat] = lng

    """Gets base url to parse
    @param lat
        latitude to replace into url
    @param lng
        Longitude to replace into url"""
    def getURL(self, lat, lng):
        config = ConfigParser.ConfigParser()
        config.read('../CONFIG/CONFIG.ini')
        url = (config.get('URL', 'forecast'))
        url = str(url).replace('latitude', str(lat)).replace('longitude', str(lng))
        print(url)
        return url

    """Gets Weather Information and Writes data to file.
    @param url
        url to parse weather for
    @param lat
        latitude of weather forecast
    @param lng
        longitude of weather forecast"""
    def getWeather(self, url, lat, lng):
        weather_data = HTML(requests.get(url).content, 'lxml')
        location = weather_data.html.body.forecast['location']
        time = weather_data.html.body.creationtime.string
        weather = weather_data.html.body.contents[0].contents[4]
        weather_forecast = Weather_Forecast(lat, lng, location, time)
        weather_forecast.detWeatherProperties(weather)
        self.weather_forecasts.append(weather_forecast)
        print(url)

    """Gets path to Output file
    @return output_file path (String)"""
    def getOutputPath(self):
        config = ConfigParser.ConfigParser()
        config.read('../CONFIG/CONFIG.ini')
        return (config.get('OUTPUT_PATH', 'output_path'))

    """Writes weather data for each {@code forecasts} to text file"""
    def outputData(self):
        out = open(self.getOutputPath(), 'a')
        for forecast in self.weather_forecasts:
            try:
                out.write('Latitude: ' + forecast.LAT)
                out.write(', Longitude: ' + forecast.LNG)
                out.write(', Day: ' + forecast.day)
                out.write(', Time: ' + forecast.time)
                out.write(', Temperature: ' + str(forecast.temperature))
                out.write(', Forecast' + forecast.forecast)
                out.write(', Chance of Precipitation: ' + str(forecast.precipitation_chance))
                out.write(', Location: ' + forecast.location + '\n')
                print('printed')
            except Exception:
                pass

    def parseWeatherData(self, lat, lng, current, total):
            url = self.getURL(lat, lng)
            try:
                self.getWeather(url, lat, lng)
                print "YES"
            except Exception:
                import sys
                error_type, error, traceback = sys.exc_info()
                print(error)
                pass
            print(str(current) + ' of ' + str(total))
            print('!' * 20)

    """Fetches weather data
    @updates contents in file"""
    def fetch(self):
        self.getAllCoordinates()
        current = 0
        total = len(self.lat_lng.keys())
        for lat, lng in self.lat_lng.items():
            self.parseWeatherData(lat, lng, current, total)
            current += 1


if __name__ == '__main__':
    weather = NationalWeather()
    weather.fetch()
    weather.outputData()